#Garden Club QR code generator
import qrcode

def generate_qr_code():
    link = input("Enter Link below for QR: ")
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR Code (1 is the smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Low error correction
        box_size=10,  # Size of each box in the QR code grid
        border=4  # Border size
    )

    qr.add_data(link)
    qr.make(fit=True)

     # Create an image from the QR Code instance
    img = qr.make_image(fill="black", back_color="white")

    # Save the QR code as a PNG file
    img.save("qrcode.png")
    print("QR code saved as 'qrcode.png'")

if __name__ == "__main__":
    generate_qr_code()