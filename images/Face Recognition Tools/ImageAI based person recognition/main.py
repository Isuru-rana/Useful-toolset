from imageai.Detection import ObjectDetection
import os
import shutil
import cv2  # OpenCV for image validation

# Initialize the object detector
execution_path = os.getcwd()
detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(os.path.join(execution_path, "yolov3.pt"))
detector.loadModel()

# Directory containing the images to process
input_directory = os.path.join(execution_path, "images")
output_directory = os.path.join(execution_path, "processed_images")

# Ensure the output directory exists
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Create directories for images with and without detected persons
person_directory = os.path.join(output_directory, "persons")
no_person_directory = os.path.join(output_directory, "no_persons")

if not os.path.exists(person_directory):
    os.makedirs(person_directory)

if not os.path.exists(no_person_directory):
    os.makedirs(no_person_directory)

# Process each image in the input directory
for file_name in os.listdir(input_directory):
    if file_name.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):  # Check if file is an image
        input_image_path = os.path.join(input_directory, file_name)

        # Validate the image file using OpenCV
        img = cv2.imread(input_image_path)
        if img is None:  # Skip if the file is unreadable
            print(f"Skipping invalid or corrupted image: {file_name}")
            continue

        try:
            # Detect objects in the image
            detections = detector.detectObjectsFromImage(
                input_image=input_image_path,
                output_image_path=os.path.join(output_directory, f"{os.path.splitext(file_name)[0]}_detected.jpg"),
                minimum_percentage_probability=30
            )

            # Check if 'person' is in the detections
            person_detected = any(eachObject["name"] == "person" for eachObject in detections)

            # Move the image to the appropriate directory
            if person_detected:
                shutil.copy(input_image_path, person_directory)
                print(f"Processed: {file_name} - Person detected")
            else:
                shutil.copy(input_image_path, no_person_directory)
                print(f"Processed: {file_name} - No person detected")

        except Exception as e:
            print(f"Error processing {file_name}: {e}")

print("Batch processing complete. Check the 'processed_images' folder.")
