import qrcode

# Get data from user
data = input("Enter the data to encode in the QR: ")

# Create a QR code object
qr = qrcode.QRCode(
    version=1,  # size of the QR code
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image of the QR code
img = qr.make_image(fill='black', back_color='white')

# Save the image
img.save("qr_code.png")

print("QR Code generated and saved as qrcode.png")
