# Automatic Face Identification Tool

This tool leverages the `face_recognition` Python package to automatically sort and organize images based on identified faces. Simply provide a folder of images, and the tool will group images containing the same face into separate folders for easy access.

## 📋 Features

- Automatically detects and groups images containing the same face.
- Organizes images into folders based on identified faces.
- Adjustable sensitivity for face identification to suit your needs.

## 🚀 How It Works

1. **Prepare Your Images**:
   - Place your images with unknown faces into the `not_sorted` folder.

2. **Run the Tool**:
   - Execute the `main.py` file:
     ```bash
     python main.py
     ```

3. **View the Results**:
   - The tool will create a new folder named `output_faces`.
   - Inside `output_faces`, you will find subfolders, each corresponding to a unique identified face.
   - Images with the same face will be grouped in the same subfolder.

## 🛠️ Adjusting Sensitivity

The sensitivity of face comparison can be adjusted using the `--tolerance` argument:

- **Default**: `0.44`
- **Lower Values**: Stricter face comparison (more precise, but may miss slight variations).
- **Higher Values**: Looser face comparison (less precise, may group similar but different faces).

Example:
```bash
python main.py --tolerance 0.35
```

If multiple faces are detected incorrectly, lower the tolerance value for better precision.

## 📦 Requirements

- Python 3.x
- Required Python package:
  ```bash
  pip install face_recognition
  ```

## 📝 Example Usage

1. Place your images into the `not_sorted` folder.
2. Run the `main.py` script:
   ```bash
   python main.py
   ```
3. Navigate to the `output_faces` folder to view sorted images.

## 🤝 Contributions

Contributions and improvements are welcome! Feel free to fork the repository, make changes, and submit a pull request.

## 📬 Contact

If you have any questions or issues, please reach out via:
- **GitHub**: [Isuru Ranaweera](https://github.com/Isuru-rana)
- **Email**: isururanawera13@gmail.com

## 📜 License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it as you like.

---

Thank you for using the Automatic Face Identification Tool! 🎉

