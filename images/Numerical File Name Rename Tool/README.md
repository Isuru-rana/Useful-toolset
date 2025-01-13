# Numerical File Name Rename Tool

This tool is designed to rename files with numerical names by adding or subtracting a specified value. It is ideal for renaming bulk files like images named in a sequential numerical format (e.g., `000001.jpg` to `003000.jpg`). The tool allows for bulk renaming with options to move or copy the renamed files.

## 📋 Features

- Add or subtract numbers to/from numerical file names.
- Handles bulk renaming efficiently.
- Provides a GUI for ease of use.
- Options to move or copy renamed files to a `rename` folder.
- Available as a Python script or a Windows executable.

## 🚀 How It Works

### Running the Tool

1. **Python Script**:
   - Run the `rename.py` script:
     ```bash
     python rename.py
     ```

2. **Windows Executable**:
   - Run `rename.exe` directly on Windows systems without requiring Python.

### Using the Tool

1. Enter the number you want to add or subtract.
2. Select whether to **Add** or **Subtract** the number.
3. Choose between:
   - **Move**: Renamed files will be moved to the `rename` folder.
   - **Copy**: Renamed files will be copied to the `rename` folder, leaving the original files intact.
4. Execute the renaming process, and the renamed files will appear in the `rename` folder.

### Example

- Input files: `000001.jpg` to `003000.jpg`
- Operation: Add `3000`
- Result: Files renamed to `003001.jpg` to `006000.jpg`

## 📦 Requirements

- Python 3.x (for the script version).
- Required Python packages (if any) are listed in `requirements.txt`.
- For the Windows executable version, no additional requirements are needed.

## 📝 Example Usage

1. Run the tool as a Python script or executable.
2. Provide the required inputs via the GUI.
3. View the renamed files in the `rename` folder.

## 🤝 Contributions

Contributions and improvements are welcome! Feel free to fork the repository, make changes, and submit a pull request.

## 📬 Contact

If you have any questions or issues, please reach out via:
- **GitHub**: [Isuru Ranaweera](https://github.com/Isuru-rana)
- **Email**: isururanawera13@gmail.com

## 📜 License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it as you like.

---

Thank you for using the Numerical File Name Rename Tool! 🎉

