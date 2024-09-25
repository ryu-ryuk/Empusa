@echo off

REM Define Flask server URL
set FLASK_SERVER=http://localhost:5000

REM Ask the user for conversion type
echo Select conversion type:
echo 1: Convert Fonts
echo 2: Compress PDF
echo 3: Convert Image
set /p choice=Enter choice (1/2/3): 

if %choice%==1 (
    REM Use PowerShell to open file dialog for font files
    for /f "delims=" %%I in ('powershell -Command "Add-Type -AssemblyName System.windows.forms; $f=[System.Windows.Forms.OpenFileDialog]::new(); $f.Multiselect=$true; $f.Filter='Font files (*.ttf)|*.ttf'; if ($f.ShowDialog() -eq 'OK') {$f.FileNames}"') do set "files=%%I"
    set /p output_dir=Enter output directory: 

    REM Loop through files and upload each to the Flask server
    for %%f in (%files%) do (
        curl -X POST %FLASK_SERVER%/convert-fonts -F "fonts=@%%f" --output "%output_dir%\%%~nxf"
    )
) else if %choice%==2 (
    REM Use PowerShell to open file dialog for PDF
    for /f "delims=" %%I in ('powershell -Command "Add-Type -AssemblyName System.windows.forms; $f=[System.Windows.Forms.OpenFileDialog]::new(); $f.Filter='PDF files (*.pdf)|*.pdf'; if ($f.ShowDialog() -eq 'OK') {$f.FileName}"') do set "input_pdf=%%I"
    set /p output_pdf=Enter output PDF name: 

    REM Compress PDF and download result
    curl -X POST %FLASK_SERVER%/compress-pdf -F "input_pdf=@%input_pdf%" -F "output_pdf=%output_pdf%" --output "%output_pdf%"
) else if %choice%==3 (
    REM Use PowerShell to open file dialog for Image
    for /f "delims=" %%I in ('powershell -Command "Add-Type -AssemblyName System.windows.forms; $f=[System.Windows.Forms.OpenFileDialog]::new(); $f.Filter='Image files (*.jpg;*.jpeg;*.png;*.gif)|*.jpg;*.jpeg;*.png;*.gif'; if ($f.ShowDialog() -eq 'OK') {$f.FileName}"') do set "input_image=%%I"
    set /p output_format=Enter output format (e.g., JPEG, PNG): 
    set /p output_dir=Enter output directory: 

    REM Convert image and download result
    curl -X POST %FLASK_SERVER%/convert-image -F "input_image=@%input_image%" -F "output_format=%output_format%" --output "%output_dir%\%~nxinput_image%"
) else (
    echo Invalid choice. Exiting.
    exit /b
)

echo Operation complete.
pause
