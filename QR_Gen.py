#Garden Club QR code generator
import qrcode
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

def generate_qr_code():
    global qr_image # Store image reference to avoid garbage collection issues
    link = url_entry.get()

    if not link.strip():
        messagebox.showerror("Error", "Please enter a valid URL!")
        return
    
    # Generate QR Code
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR Code (1 is the smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Low error correction
        box_size=10,  # Size of each box in the QR code grid
        border=4  # Border size
    )

    qr.add_data(link)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    global img
    img = qr.make_image(fill="black", back_color="white")

    # Convert image for Tkinter display
    qr_image = ImageTk.PhotoImage(img)
    qr_label.config(image=qr_image)
    qr_label.image = qr_image  # Keep reference
    save_button.config(state=tk.NORMAL)  # Enable save button


def save_qr():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        img.save(file_path)
        messagebox.showinfo("Success", "QR Code saved successfully!")
    else:
        messagebox.showwarning("Error", "Error saving QR Code.")

# Create GUI window
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("600x800")
root.resizable(False, False)

# URL Entry Field
tk.Label(root, text="Enter URL:", font=("Arial", 12)).pack(pady=10)
url_entry = tk.Entry(root, width=40, font=("Arial", 12))
url_entry.pack(pady=5)

# Generate Button
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr_code, font=("Arial", 12), bg="blue", fg="black")
generate_button.pack(pady=10)

# QR Code Display
qr_label = tk.Label(root)
qr_label.pack(pady=10)

# Save Button
save_button = tk.Button(root, text="Save QR Code", command=save_qr, font=("Arial", 12), bg="green", fg="black", state=tk.DISABLED)
save_button.pack(pady=10)

# Run the application
root.mainloop()