import qrcode
# You can also customize the QR code by using the qrcode.QRCode class. Here's an example of how to create a QR code with custom settings:   
qr=qrcode.QRCode(
    version=1,  # controls the size of the QR code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # controls the error correction level
    box_size=10,  # controls how many pixels each "box" of the QR code is
    border=4,  # controls how many boxes thick the border should b
)

# Add data
qr.add_data("https://github.com/FarhanHussain7")
qr.make(fit=True)

# Generate the image with custom colors
img = qr.make_image(fill_color="black", back_color="red")

# Save and show
img.save("Colour_QRcode.png")
img.show()

# new line added to the code