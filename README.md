
```

 (`-')  _<-. (`-')   _  (`-')            (`-').-> (`-')  _  
 ( OO).-/   \(OO )_  \-.(OO )     .->    ( OO)_   (OO ).-/  
(,------.,--./  ,-.) _.'    \,--.(,--.  (_)--\_)  / ,---.   
 |  .---'|   `.'   |(_...--''|  | |(`-')/    _ /  | \ /`.\  
(|  '--. |  |'.'|  ||  |_.' ||  | |(OO )\_..`--.  '-'|_.' | 
 |  .--' |  |   |  ||  .___.'|  | | |  \.-._)   \(|  .-.  | 
 |  `---.|  |   |  ||  |     \  '-'(_ .'\       / |  | |  | 
 `------'`--'   `--'`--'      `-----'    `-----'  `--' `--' 
```

# Empusa 
A web application for converting files between various formats (e.g., images, fonts, and PDFs) using Flask and cloud storage.

## Overview 🌐
**Empusa** is a versatile web-based platform designed to make file conversions fast and reliable. Empusa supports a variety of formats and compression options, with a user-friendly interface powered by Flask.

## Features ✨
- **File Upload 📤**: Users can upload files for conversion.
- **Supported Conversions 🔄**:
  - Fonts: **TTF ➡️ OTF** conversion.
  - Images: Supports conversion between **JPEG**, **PNG**, **GIF**, **BMP**, and **TIFF** formats.
  - PDF Compression: Compress PDFs with different size options.

## Current Limitations 🚧
As of today, the following features are operational:
- **TTF to OTF** font conversion.
- Image format conversion between **JPEG**, **PNG**, **GIF**, **BMP**, and **TIFF**.
- **PDF compression**.

## Planned Features 🔧
- **CLI Interface Tool 💻**: I am actively working on transforming this project into a command-line interface tool for easy use across platforms.
- **Custom Compression Options 🔍**: Fine-tune compression for images and PDFs (low, medium, high).
- **Additional Conversion Formats 🛠️**: More file types such as DOCX, XLSX, and more image/audio formats will be supported soon.
- **Refinements**: Refine and properly document about the tool's function and usage on both windows and linux using scripts.

- **Cloud Storage Integration ☁️**: Empusa will integrate with AWS S3 or Google Cloud Storage to store and manage your converted files.
 
- 
## Getting Started 🚀
1. Clone the repository: 
    ```bash
    git clone https://github.com/ryu-ryuk/empusa.git
    ```
2. Install the necessary dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the Flask server:
    ```bash
    flask run
    ```

## Soon to Exist 🌱
Work on the CLI tool and additional file format conversions is in progress. Keep an eye out for future updates! 💡

---

Built with ♡ by [ryu-ryuk](https://github.com/ryu-ryuk)
