import numpy as np
from PIL import Image
from tkinter import filedialog, Tk

Tk().withdraw()
file_path = filedialog.askopenfilename(
    title="Select an image",
    filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp *.tiff")]
)
if not file_path:
    print("❌ No image selected.")
    exit()
image = Image.open(file_path).convert("RGB")
data = np.array(image)
key = 123 
choice = input("Choose mode: (e) Encrypt | (d) Decrypt: ").lower()

if choice == 'e':
    encrypted_data = data ^ key   
    encrypted_data = np.flipud(encrypted_data)   
    Image.fromarray(encrypted_data).save("encrypted_image.png")
    print("✅ Image encrypted and saved as 'encrypted_image.png'")
elif choice == 'd':    
    encrypted_data = np.array(image)    
    decrypted_data = np.flipud(encrypted_data)    
    decrypted_data = decrypted_data ^ key    
    Image.fromarray(decrypted_data).save("decrypted_image.png")
    print("🔓 Image decrypted and saved as 'decrypted_image.png'")
else:
    print("⚠️ Invalid choice! Please enter 'e' or 'd'.")