import os
from fontTools.ttLib import TTFont
from flask import request, render_template

def convert_fonts():
    try:
        files = request.files.getlist('fonts')  # Get the list of uploaded font files
        output_paths = []  # Store the paths of converted fonts
        
        # Ensure the 'uploads/fonts' directory exists
        if not os.path.exists('uploads/fonts'):
            os.makedirs('uploads/fonts')
        
        # Save uploaded font files
        for font_file in files:
            font_file.save(os.path.join('uploads/fonts', font_file.filename))
        
        # Process the saved files for conversion
        convert_fonts_in_directory('uploads/fonts')
        
        # Collect the converted file paths
        for filename in os.listdir('uploads/fonts'):
            if filename.endswith('.ttf') or filename.endswith('.otf'):  # Include .ttf and .otf
                output_paths.append(os.path.join('uploads/fonts', filename))
        
        # Render the download page with the list of converted files
        return render_template('download.html', files=output_paths)
    
    except Exception as e:
        return str(e), 500  # Return error if exception occurs

# Font conversion helper functions
def convert_fonts_in_directory(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if filename.endswith(".otf"):
            convert_otf_to_ttf(file_path)
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
