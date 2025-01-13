import os
import shutil
from PIL import Image
import face_recognition

# Paths to folders
raw_sorted_path = "./raw_images"
not_sorted_path = "./not_sorted"

# Create the not_sorted folder if it doesn't exist
os.makedirs(not_sorted_path, exist_ok=True)

# Loop through all files in the raw_sorted folder
for filename in os.listdir(raw_sorted_path):
    file_path = os.path.join(raw_sorted_path, filename)
    
    # Check if the file is an image
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        try:
            # Load the image
            image = face_recognition.load_image_file(file_path)
            
            # Detect faces in the image
            face_locations = face_recognition.face_locations(image)
            
            # If faces are found, move the file to the not_sorted folder
            if len(face_locations) > 0:
                print(f"Found {len(face_locations)} face(s) in {filename}. Moving to not_sorted.")
                shutil.move(file_path, os.path.join(not_sorted_path, filename))
            else:
                print(f"No faces found in {filename}.")
        
        except Exception as e:
            print(f"Error processing {filename}: {e}")
