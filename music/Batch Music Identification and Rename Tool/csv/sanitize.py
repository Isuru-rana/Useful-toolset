import pandas as pd

# Load the CSV file
file_path = r"sanitized_music.csv"  # Replace with your file path
audio_metadata_df = pd.read_csv(file_path)

# Define a function to sanitize column data
def sanitize_column(data):
    invalid_chars = r'\/:*?"<>|'
    if isinstance(data, str):
        for char in invalid_chars:
            data = data.replace(char, "_")
    return data

# Sanitize the 'title', 'album_name', and 'artists_names' columns
columns_to_sanitize = ['title', 'album_name', 'artists_names']
for column in columns_to_sanitize:
    if column in audio_metadata_df.columns:
        audio_metadata_df[column] = audio_metadata_df[column].apply(sanitize_column)

# Save the sanitized DataFrame to a new CSV file
sanitized_file_path = r"sanitized_output.csv"  # Replace with your desired output path
audio_metadata_df.to_csv(sanitized_file_path, index=False)

print(f"Sanitized CSV saved to {sanitized_file_path}")
