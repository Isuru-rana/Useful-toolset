import os
import shutil
import threading
from tkinter import Tk, Label, Entry, Button, Text, Checkbutton, IntVar, filedialog, Scrollbar, RIGHT, Y, END, StringVar, OptionMenu, Frame, Toplevel
from tkinter.ttk import Progressbar

def rename_files_thread():
    folder_path = filedialog.askdirectory(title="Select Folder")
    if not folder_path:
        return

    # Create a new folder named 'renamed'
    renamed_folder = os.path.join(folder_path, "renamed")
    if not os.path.exists(renamed_folder):
        os.makedirs(renamed_folder)

    operation = add_or_subtract.get()
    action = action_choice.get()
    try:
        value = int(number_entry.get())
    except ValueError:
        log_message("Invalid number entered. Please enter a valid integer.")
        return

    number_format = 5
    files = [item for item in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, item))]
    total_files = len(files)

    if total_files == 0:
        log_message("No files found in the selected folder.")
        return

    progress_bar["maximum"] = total_files
    progress_bar["value"] = 0

    processed_files = 0
    skipped_files = 0

    for item in files:
        item_path = os.path.join(folder_path, item)

        try:
            if "_" in item:
                parts = item.split("_")
                numeric_part = int(parts[0])
                suffix = f"_{parts[1]}"
            else:
                numeric_part = int(item.split(".")[0])
                suffix = f".{item.split('.')[-1]}"

            new_number = numeric_part + value if operation else numeric_part - value
            formatted_number = f"{new_number:0{number_format}d}"
            new_filename = f"{formatted_number}{suffix}"
            new_file_path = os.path.join(renamed_folder, new_filename)

            # Check if the new file name already exists in the renamed folder
            if os.path.exists(new_file_path):
                log_message(f"Skipping file (already exists in 'renamed'): {new_filename}")
                skipped_files += 1
            else:
                if action == "Copy":
                    shutil.copy(item_path, new_file_path)
                    log_message(f"Copied: {item} -> renamed/{new_filename}")
                elif action == "Move":
                    os.rename(item_path, new_file_path)
                    log_message(f"Moved: {item} -> renamed/{new_filename}")
                processed_files += 1
        except ValueError:
            log_message(f"Skipping invalid file: {item}")

        progress_bar["value"] = processed_files
        root.update_idletasks()  # Update UI to reflect progress bar changes

    log_message(f"Process completed. Total files processed: {processed_files}, Skipped: {skipped_files}")

    # Schedule the popup to appear after the processing is finished
    root.after(500, show_summary_popup, processed_files, skipped_files)

def log_message(message):
    output_box.insert(END, message + "\n")
    output_box.see(END)

def toggle_status_section():
    if output_frame.winfo_ismapped():
        output_frame.pack_forget()
    else:
        output_frame.pack()

def show_summary_popup(processed_files, skipped_files):
    summary_popup = Toplevel(root)
    summary_popup.title("Renaming Completed")

    # Set fixed size for the popup and remove maximize/minimize buttons
    summary_popup.geometry("300x200")
    summary_popup.resizable(False, False)  # Disable resizing
    
    # Popup will now have close button and title bar with close icon
    Label(summary_popup, text=f"Renaming completed!\n\nFiles Renamed: {processed_files}\nFiles Skipped: {skipped_files}", padx=20, pady=20).pack()
    Button(summary_popup, text="Close", command=summary_popup.destroy).pack(pady=10)

def start_rename_process():
    rename_thread = threading.Thread(target=rename_files_thread)
    rename_thread.start()

# Create the GUI
root = Tk()
root.title("IIZO Rename Tool v1.0.0")

# Set the main window to be non-resizable
root.resizable(False, False)

# Instruction labels
Label(root, text="Enter a number to add or subtract:").pack()

# Entry for the number
number_entry = Entry(root, width=10)
number_entry.pack()

# Checkboxes for Add/Subtract
add_or_subtract = IntVar()
add_checkbox = Checkbutton(root, text="Add", variable=add_or_subtract, onvalue=1, offvalue=0)
add_checkbox.pack()

subtract_checkbox = Checkbutton(root, text="Subtract", variable=add_or_subtract, onvalue=0, offvalue=1)
subtract_checkbox.pack()

# Dropdown for action (Copy/Move)
Label(root, text="Choose Action:").pack()
action_choice = StringVar(root)
action_choice.set("Move")  # Default action is Move
action_menu = OptionMenu(root, action_choice, "Move", "Copy")
action_menu.pack()

# Start button
start_button = Button(root, text="Start Processing", command=start_rename_process)
start_button.pack()

# Progress bar
Label(root, text="Progress:").pack()
progress_bar = Progressbar(root, orient="horizontal", length=400, mode="determinate")
progress_bar.pack()

# Collapsible Processing Status checkbox (left bottom)
show_status_var = IntVar()
status_checkbox = Checkbutton(root, text="Show Processing Status", variable=show_status_var, command=toggle_status_section)
status_checkbox.pack(anchor="w", padx=10, pady=5)

# Output log (initially hidden)
output_frame = Frame(root)
scrollbar = Scrollbar(output_frame)
scrollbar.pack(side=RIGHT, fill=Y)

output_box = Text(output_frame, height=6, width=50, yscrollcommand=scrollbar.set)
output_box.pack()
scrollbar.config(command=output_box.yview)

# Run the GUI
root.mainloop()
