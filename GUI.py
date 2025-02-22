import os
import shutil
import zipfile
import tkinter as tk
from tkinter import filedialog, messagebox
import s3_manager

# ✅ Extraction Path
EXTRACTION_PATH = "website_files/"

def clear_extraction_folder():
    """ Deletes old extracted files before extracting a new ZIP file """
    if os.path.exists(EXTRACTION_PATH):
        shutil.rmtree(EXTRACTION_PATH)  # Remove old files
    os.makedirs(EXTRACTION_PATH)  # Recreate the folder

def extract_zip(zip_path):
    """ Extracts the uploaded ZIP file into the designated folder """
    try:
        clear_extraction_folder()  # Remove previous files
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(EXTRACTION_PATH)  # Extract new files
        messagebox.showinfo("Success", f"Files extracted to: {EXTRACTION_PATH}")
        return True  # Extraction successful
    except zipfile.BadZipFile:
        messagebox.showerror("Error", "Invalid ZIP file! Please select a valid ZIP file.")
        return False  # Extraction failed

def copy_to_clipboard():
    """ Copies the deployment URL to the clipboard """
    root.clipboard_clear()  # Clear the clipboard
    root.clipboard_append(lbl_url["text"])  # Copy the deployment URL
    root.update()  # Update clipboard content
    messagebox.showinfo("Copied!", "Deployment URL copied to clipboard!")

def upload_and_deploy():
    """ Handles ZIP file upload, extraction, S3 upload, and deployment """
    file_path = filedialog.askopenfilename(filetypes=[("ZIP Files", "*.zip")])  # Open file dialog
    
    if file_path:
        lbl_file.config(text=f"Selected: {os.path.basename(file_path)}")  # Update label
        if extract_zip(file_path):  # If extraction is successful
            deployment_id = s3_manager.generate_unique_id()  # Generate unique ID
            s3_manager.upload_files_to_s3(EXTRACTION_PATH, deployment_id)  # Upload files
            s3_manager.configure_static_website()  # Enable website hosting
            deployment_url = s3_manager.get_deployment_url(deployment_id)  # Get deployment link
            
            # ✅ Show the deployment URL in the GUI
            lbl_url.config(text=deployment_url, fg="blue")

            # ✅ Enable the "Copy Link" button
            btn_copy.config(state=tk.NORMAL)

            messagebox.showinfo("Deployment Successful", f"Your website is live at:\n{deployment_url}")

# ✅ Create the GUI
root = tk.Tk()
root.title("ZIP File Extractor & Uploader")
root.geometry("500x300")

# ✅ Upload Button
btn_upload = tk.Button(root, text="Upload & Deploy ZIP", command=upload_and_deploy, padx=10, pady=5)
btn_upload.pack(pady=10)

# ✅ Label to show selected file
lbl_file = tk.Label(root, text="No file selected", fg="gray")
lbl_file.pack()

# ✅ Label to display deployment URL
lbl_url = tk.Label(root, text="", fg="blue", wraplength=400, justify="center")
lbl_url.pack(pady=5)

# ✅ Copy Button (Initially Disabled)
btn_copy = tk.Button(root, text="Copy Link", command=copy_to_clipboard, padx=10, pady=5, state=tk.DISABLED)
btn_copy.pack(pady=5)

# ✅ Start GUI loop
if __name__ == '__main__':
    root.mainloop()
