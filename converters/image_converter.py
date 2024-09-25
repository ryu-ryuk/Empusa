from PIL import Image
import os

def convert_image(input_image_path, output_format):
    # Open the input image
    img = Image.open(input_image_path)

    # Generate output image path
    base_name = os.path.splitext(input_image_path)[0]
    output_image_path = f"{base_name}.{output_format.lower()}"  # Ensure the extension is lower case

    # Save the image in the desired format
    img.save(output_image_path, output_format.upper())
    
    return output_image_path  # Return the path to the converted image
