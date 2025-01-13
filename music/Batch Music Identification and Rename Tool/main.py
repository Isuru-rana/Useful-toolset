import os
from shutil import move
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3
import pandas as pd

# Specify the relative paths
csv_file_path = os.path.join("output", "sanitized_music.csv")
audio_files_directory = os.path.join(".", "Music")  # Current directory + "Music"
fixed_files_directory = os.path.join(audio_files_directory, "fixed")

# Load the CSV file
audio_metadata_df = pd.read_csv(csv_file_path)

# Create the "fixed" directory if it doesn't exist
os.makedirs(fixed_files_directory, exist_ok=True)

# Iterate over the rows of the CSV file
for index, row in audio_metadata_df.iterrows():
    filename = row['filename']
    title = row.get('title', None)
    artist = row.get('artists_names', None)  # Get artist from the 'artists_names' column
    album_name = row.get('album_name', None)
    genre = row.get('genre', None)

    # Full path to the audio file
    audio_file_path = os.path.join(audio_files_directory, filename)

    # Check if the audio file exists and title is available
    if os.path.isfile(audio_file_path) and title:
        try:
            # Load the audio file using mutagen
            audio = ID3(audio_file_path)

            # Remove all album art tags
            audio.delall("APIC")
            audio.save()

            # Add or update metadata
            audio_tags = EasyID3(audio_file_path)
            audio_tags["title"] = title
            audio_tags["artist"] = artist
            if album_name:
                audio_tags["album"] = album_name
            if genre:
                audio_tags["genre"] = genre
            audio_tags.save()

            # Create the new filename as "title - artist.mp3"
            new_filename = f"{title} - {artist}.mp3"
            new_file_path = os.path.join(fixed_files_directory, new_filename)

            # Move the file to the "fixed" directory
            move(audio_file_path, new_file_path)

            print(f"Updated and moved: {filename} -> {new_filename}")
        except Exception as e:
            print(f"Error updating {filename}: {e}")
    else:
        print(f"Skipped: {filename} (No title found or file not found)")
