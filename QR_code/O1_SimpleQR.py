import qrcode

# Create a QR code object
img=qrcode.make("https://github.com/FarhanHussain7")

# Save the QR code as an image file
img.save("Farhan_QRcode.png")
# Display the QR code
img.show()
