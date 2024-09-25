from flask import Flask, request, render_template, send_from_directory
from converters.font_converter import convert_fonts_in_directory
from converters.pdf_converter import compress_pdf
from converters.image_converter import convert_image
import os

app = Flask(__name__)

# Ensure upload directories exist
os.makedirs('uploads/fonts', exist_ok=True)
os.makedirs('uploads/pdfs', exist_ok=True)
os.makedirs('uploads/images', exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/convert-fonts', methods=['POST'])
def convert_fonts():
    try:
        files = request.files.getlist('fonts')  # Get the list of uploaded font files
        output_paths = []  # Store the paths of converted fonts
        
        for font_file in files:
            font_file.save(os.path.join('uploads/fonts', font_file.filename))  # Save each file
        
        convert_fonts_in_directory('uploads/fonts')  # Process the saved files
        
        # Add converted font file paths to output_paths
        for filename in os.listdir('uploads/fonts'):
            if filename.endswith('.ttf'):  # Assuming converted files are .ttf
                output_paths.append(os.path.join('uploads/fonts', filename))
        
        return render_template('download.html', files=output_paths)
    
    except Exception as e:
        return str(e), 500  # Return the error message for debugging

@app.route('/compress-pdf', methods=['POST'])
def compress_pdf_route():
    try:
        input_pdf = request.files['input_pdf']
        output_pdf_name = request.form['output_pdf']
        
        # Ensure the output file name has a .pdf extension
        if not output_pdf_name.endswith('.pdf'):
            output_pdf_name += '.pdf'

        input_pdf_path = os.path.join('uploads/pdfs', input_pdf.filename)
        output_pdf_path = os.path.join('uploads/pdfs', output_pdf_name)

        input_pdf.save(input_pdf_path)  # Save the uploaded PDF
        compress_pdf(input_pdf_path, output_pdf_path)  # Compress the saved PDF

        return render_template('download.html', files=[output_pdf_path])
    
    except Exception as e:
        return str(e), 500  # Return the error message for debugging

@app.route('/convert-image', methods=['POST'])
def convert_image_route():
    try:
        input_image = request.files['input_image']
        output_format = request.form['output_format'].strip().upper()  # Normalize to uppercase and strip whitespace
        input_image_path = os.path.join('uploads/images', input_image.filename)

        # Save the uploaded image
        input_image.save(input_image_path)  

        # Ensure the output format is valid
        valid_formats = ['JPEG', 'PNG', 'GIF', 'BMP', 'TIFF'] 
        if output_format not in valid_formats:
            return "Invalid output format. Supported formats: " + ", ".join(valid_formats), 400

        # Generate the output image path inside the route
        output_image_path = os.path.splitext(input_image_path)[0] + '.' + output_format.lower()  # Create output path

        # Call the convert_image function with both input and output paths
        converted_image_path = convert_image(input_image_path, output_format)

        return render_template('download.html', files=[converted_image_path])

    except Exception as e:
        return str(e), 500  # Return the error message for debugging

@app.route('/download/<path:filename>')
def download_file(filename):
    try:
        directory = os.path.dirname(filename)
        return send_from_directory('uploads/images', filename, as_attachment=True)

    
    except Exception as e:
        return str(e), 500  # Return the error message for debugging

if __name__ == "__main__":
    app.run(debug=True)
