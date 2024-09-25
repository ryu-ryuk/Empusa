import os
from fontTools.ttLib import TTFont
import argparse

# Font conversion helper functions
def convert_fonts_in_directory(directory):
    """
    Converts all .otf files to .ttf and .ttf files to .otf in the specified directory.
    """
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if filename.endswith(".otf"):
            convert_otf_to_ttf(file_path)
        elif filename.endswith(".ttf"):
            convert_ttf_to_otf(file_path)

def convert_otf_to_ttf(otf_file_path):
    """
    Converts a given .otf file to .ttf format.
    """
    font = TTFont(otf_file_path)
    base_name = os.path.splitext(os.path.basename(otf_file_path))[0]
    ttf_file_path = os.path.join(os.path.dirname(otf_file_path), base_name + ".ttf")
    font.save(ttf_file_path)
    print(f"Converted {otf_file_path} to {ttf_file_path}")

def convert_ttf_to_otf(ttf_file_path):
    """
    Converts a given .ttf file to .otf format.
    """
    font = TTFont(ttf_file_path)
    base_name = os.path.splitext(os.path.basename(ttf_file_path))[0]
    otf_file_path = os.path.join(os.path.dirname(ttf_file_path), base_name + ".otf")
    font.save(otf_file_path)
    print(f"Converted {ttf_file_path} to {otf_file_path}")

# Main entry point for command-line execution
def main():
    """
    This function sets up command-line arguments for the script and calls the font conversion process.
    """
    parser = argparse.ArgumentParser(description="Convert fonts between OTF and TTF formats.")
    parser.add_argument('--input', type=str, required=True, help="Input font file or directory.")
    parser.add_argument('--output', type=str, required=True, help="Output directory for converted fonts.")

    args = parser.parse_args()

    input_path = args.input
    output_directory = args.output

    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Check if input is a file or directory
    if os.path.isdir(input_path):
        # Copy input fonts to the output directory
        for file_name in os.listdir(input_path):
            full_file_path = os.path.join(input_path, file_name)
            if file_name.endswith(('.ttf', '.otf')):
                os.system(f"cp {full_file_path} {output_directory}")
    elif os.path.isfile(input_path):
        if input_path.endswith(('.ttf', '.otf')):
            os.system(f"cp {input_path} {output_directory}")
    else:
        print(f"Invalid input path: {input_path}")
        return

    # Convert fonts in the output directory
    convert_fonts_in_directory(output_directory)

if __name__ == "__main__":
    main()
