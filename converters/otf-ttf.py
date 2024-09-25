from fontTools.ttLib import TTFont
import os
from tkinter import Tk
from tkinter import filedialog

def convert_otf_to_ttf(otf_file_path):

    '''define objects'''

    font = TTFont(otf_file_path)
    base_name = os.path.splitext(os.path.basename(otf_file_path))[0]
    ttf_file_path = os.path.join(os.path.dirname(otf_file_path), base_name + ".ttf")
    font.save(ttf_file_path)

    print(f"Converted {otf_file_path} to {ttf_file_path}")

# Function to select directory using a graphical dialog
def select_directory():
    root = Tk()
    root.withdraw()  # Hide the main tkinter window
    directory = filedialog.askdirectory(title="Select Directory Containing .otf Files")
    return directory

# Use graphical directory selection
otf_directory = select_directory()

if not otf_directory:
    print("No directory selected. Exiting...")
else:
    # Iterate through all the files in the directory
    for filename in os.listdir(otf_directory):
        # Check the ".otf" extension
        if filename.endswith(".otf"):
            # Construct the full path
            otf_file_path = os.path.join(otf_directory, filename)
            # Call the function to convert .otf to .ttf
            convert_otf_to_ttf(otf_file_path)
