
# QR Code Generator

This is a simple Python-based QR Code Generator that allows users to create QR codes from any text or URL. The QR code is generated and saved as an image file (PNG format).

## Features
- Generate QR codes from any text or URL.
- Save the generated QR code as an image (PNG).
- Easy-to-use command-line interface.

## Prerequisites
Before running the project, make sure you have Python installed on your machine. You will also need to install the following Python library:
1. `qrcode[pil]` - For generating QR codes.

### Installation
Use the following command to install the required libraries:

```bash
pip install qrcode[pil]
```

### Usage
1. Clone the repository or download the project files.
2. Run the script `qr_generator.py` and enter the text or URL you want to encode.
3. The QR code will be generated and saved as an image file (`qrcode.png`) in the same directory.

```bash
python qr_generator.py
```

### Example
Here is a sample of how to generate a QR code:

```python
Enter the data to encode in the QR code: https://example.com
QR Code generated and saved as qrcode.png
```

After running the script, you will find the `qrcode.png` file in the project directory.

