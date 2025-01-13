# Bulk Person Recognition Tool

This tool utilizes the `ImageAI` Python package to detect and classify images based on the presence of persons. It automates the process of sorting images into separate folders based on whether a person is detected in the image or not.

## 📋 Features

- Detects the presence of persons in images.
- Automatically sorts images into folders:
  - `processed_images/persons`: For images containing persons.
  - `processed_images/no_persons`: For images without persons.
- Uses the YOLOv3 model and the default dataset from `ImageAI` for person recognition.

## 🚀 How It Works

1. **Prepare Your Images**:
   - Place all your images into the `images` folder.

2. **Download the YOLOv3 Model**:
   - Download the YOLOv3 model file from [here](https://github.com/OlafenwaMoses/ImageAI/releases/download/3.0.0-pretrained/yolov3.pt).
   - Copy the downloaded `yolov3.pt` file into the tool folder.

3. **Run the Tool**:
   - Execute the `main.py` file:
     ```bash
     python main.py
     ```

4. **View the Results**:
   - Images containing persons will be moved to `processed_images/persons`.
   - Images without persons will be moved to `processed_images/no_persons`.

## 📦 Requirements

- Python 3.x
- Required Python packages:
  ```bash
  pip install imageai
  ```

## 📝 Example Usage

1. Place your images into the `images` folder.
2. Download and place the YOLOv3 model file into the tool folder.
3. Run the `main.py` script:
   ```bash
   python main.py
   ```
4. Navigate to the `processed_images/persons` folder for images containing persons, or `processed_images/no_persons` for those without persons.

## 🤝 Contributions

Contributions and improvements are welcome! Feel free to fork the repository, make changes, and submit a pull request.

## 📬 Contact

If you have any questions or issues, please reach out via:
- **GitHub**: [Isuru Ranaweera](https://github.com/Isuru-rana)
- **Email**: isururanawera13@gmail.com

## 📜 License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it as you like.

---

Thank you for using the Bulk Person Recognition Tool! 🎉

