from fontTools.ttLib import TTFont
import os

def convert_fonts_in_directory(directory):
    # Iterate through all files in the provided directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        # Check for .otf files
        if filename.endswith(".otf"):
            convert_otf_to_ttf(file_path)
        # Check for .ttf files
        elif filename.endswith(".ttf"):
            convert_ttf_to_otf(file_path)

def convert_otf_to_ttf(otf_file_path):
    font = TTFont(otf_file_path)
    base_name = os.path.splitext(os.path.basename(otf_file_path))[0]
    ttf_file_path = os.path.join(os.path.dirname(otf_file_path), base_name + ".ttf")
    font.save(ttf_file_path)
    print(f"Converted {otf_file_path} to {ttf_file_path}")

def convert_ttf_to_otf(ttf_file_path):
    font = TTFont(ttf_file_path)
    base_name = os.path.splitext(os.path.basename(ttf_file_path))[0]
    otf_file_path = os.path.join(os.path.dirname(ttf_file_path), base_name + ".otf")
    font.save(otf_file_path)
    print(f"Converted {ttf_file_path} to {otf_file_path}")
