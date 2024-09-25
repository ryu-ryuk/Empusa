#!/bin/bash

# Define Flask server URL (change if running on a different IP or port)
FLASK_SERVER="http://localhost:5000"

# Select file type
echo "Select conversion type:"
echo "1: Convert Fonts"
echo "2: Compress PDF"
echo "3: Convert Image"
read choice

# File dialog using zenity to select files
if [[ "$choice" == "1" ]]; then
    files=$(zenity --file-selection --multiple --title="Select Fonts to Convert")
    output=$(zenity --entry --title="Specify output directory" --text="Enter output directory:")
    IFS="|" read -r -a file_array <<< "$files"
    
    # Convert fonts by uploading files to Flask
    for file in "${file_array[@]}"; do
        curl -X POST "$FLASK_SERVER/convert-fonts" -F "fonts=@$file" --output "$output/$(basename $file)"
    done

elif [[ "$choice" == "2" ]]; then
    input_pdf=$(zenity --file-selection --title="Select PDF to Compress")
    output_pdf=$(zenity --entry --title="Specify output PDF name" --text="Enter the output PDF name:")
    
    # Compress PDF by uploading to Flask
    curl -X POST "$FLASK_SERVER/compress-pdf" -F "input_pdf=@$input_pdf" -F "output_pdf=$output_pdf" --output "$output_pdf"

elif [[ "$choice" == "3" ]]; then
    input_image=$(zenity --file-selection --title="Select Image to Convert")
    output_format=$(zenity --entry --title="Specify Output Format" --text="Enter output format (e.g., JPEG, PNG, GIF):")
    output_dir=$(zenity --entry --title="Specify Output Directory" --text="Enter output directory:")
    
    # Convert image by uploading to Flask
    curl -X POST "$FLASK_SERVER/convert-image" -F "input_image=@$input_image" -F "output_format=$output_format" --output "$output_dir/$(basename $input_image)"
else
    echo "Invalid choice"
    exit 1
fi

echo "Operation complete."
