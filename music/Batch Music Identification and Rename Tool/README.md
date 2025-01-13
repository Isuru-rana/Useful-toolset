# Batch Music Identification and Rename Tool

This tool streamlines the process of identifying and renaming music files using the ACRCloud API. It combines multiple scripts to handle identification, data sanitization, and renaming, ensuring your music library is organized with accurate metadata.

## 📋 Features

- Identifies music files using the ACRCloud API.
- Sanitizes metadata for consistency and accuracy.
- Renames and organizes music files based on identified metadata.
- Handles unidentified files separately for further review.

## 🚀 How It Works

### Step 1: Set Up ACRCloud

1. Clone the original ACRCloud repository to your system:
   ```bash
   git clone https://github.com/acrcloud/acrcloud_scan_files_python3.git
   ```
2. Create an account on [ACRCloud](https://www.acrcloud.com/).
3. Create a new project under **Projects > Audio & Video Recognition Project**.
4. Note the `Host`, `Access Key`, and `Secret Key` provided by ACRCloud.
5. Open the `config.yaml.example` file in the cloned repository and rename it to `config.yaml`.
6. Add the `Host`, `Access Key`, and `Secret Key` to the `config.yaml` file.

### Step 2: Identify Music Files

1. Run the following command to identify music files:
   ```bash
   python main.py -t <music_file_location> -o <output_csv_file_location> --no-duration -c music -s 40 -e 50
   ```
   Example:
   ```bash
   python main.py -t "C:\Users\isuru\OneDrive\Desktop\Music\" -o C:\Users\isuru\OneDrive\Desktop\Music\output --no-duration -c music -s 40 -e 50
   ```
2. This will create a CSV file with metadata for the identified music files. Save this file for further processing.

### Step 3: Sanitize Metadata

1. Copy the folder containing this tool to your system if not already done.
2. Place the generated CSV file into the `csv` folder.
3. Run the sanitize script to clean and fix issues in the CSV file:
   ```bash
   python sanitize.py
   ```

### Step 4: Rename and Organize Music Files

1. Copy your music files into the `music` folder.
2. Run the main script to rename and organize files:
   ```bash
   python main.py
   ```
3. Processed music files will be:
   - Moved to the `fixed` folder with updated names based on metadata.
   - Files that could not be identified will remain in the `music` folder.

## 📦 Requirements

- Python 3.x
- Required Python packages (refer to `requirements.txt` in the cloned repository).
- ACRCloud account and project.

## 📝 Example Workflow

1. Clone the ACRCloud repository and configure it.
2. Identify music files to generate a metadata CSV.
3. Sanitize the metadata using the sanitize script.
4. Rename and organize music files with the main script.

## 🤝 Contributions

Contributions and improvements are welcome! Feel free to fork the repository, make changes, and submit a pull request.

## 📬 Contact

If you have any questions or issues, please reach out via:
- **GitHub**: [Isuru Ranaweera](https://github.com/Isuru-rana)
- **Email**: isururanawera13@gmail.com

## 📜 License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it as you like.

---

Thank you for using the Batch Music Identification and Rename Tool! 🎉

