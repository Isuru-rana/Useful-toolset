import face_recognition
import os
import shutil
import argparse

# Argument parser for configurable options
parser = argparse.ArgumentParser(description="Face grouping and sorting tool.")
parser.add_argument("--input", type=str, default="not_sorted", help="Folder containing unsorted images.")
parser.add_argument("--output", type=str, default="output_faces", help="Folder to save grouped images.")
parser.add_argument("--tolerance", type=float, default=0.44, help="Set the face comparison tolerance (default: 0.44). Lower values are stricter.")
args = parser.parse_args()

# Directories
INPUT_DIR = args.input
OUTPUT_DIR = args.output

# Ensure the output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

print("Processing images and grouping by similarity...")

# Initialize groups of known faces
face_groups = []
group_names = []

# Process each image in the input folder
files = [f for f in os.listdir(INPUT_DIR) if f.endswith((".jpg", ".png"))]
for i, filename in enumerate(files):
    image_path = os.path.join(INPUT_DIR, filename)
    image = face_recognition.load_image_file(image_path)
    face_encodings = face_recognition.face_encodings(image)

    if not face_encodings:
        print(f"[{i+1}/{len(files)}] No faces detected in {filename}.")
        continue

    face_encoding = face_encodings[0]  # Assume one face per image for simplicity
    matched_group = None

    # Compare with existing groups
    for group_index, group_face_encoding in enumerate(face_groups):
        matches = face_recognition.compare_faces([group_face_encoding], face_encoding, tolerance=args.tolerance)
        if True in matches:
            matched_group = group_index
            break

    # If matched, add to the group
    if matched_group is not None:
        group_name = group_names[matched_group]
        group_dir = os.path.join(OUTPUT_DIR, group_name)
        os.makedirs(group_dir, exist_ok=True)
        shutil.copy(image_path, os.path.join(group_dir, filename))
        print(f"[{i+1}/{len(files)}] {filename} -> Group: {group_name}")
    else:
        # Create a new group
        new_group_name = f"group_{len(face_groups) + 1}"
        face_groups.append(face_encoding)
        group_names.append(new_group_name)

        group_dir = os.path.join(OUTPUT_DIR, new_group_name)
        os.makedirs(group_dir, exist_ok=True)
        shutil.copy(image_path, os.path.join(group_dir, filename))
        print(f"[{i+1}/{len(files)}] {filename} -> New Group: {new_group_name}")

print(f"\nProcessing complete. Results saved in '{OUTPUT_DIR}'.")
