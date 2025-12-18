from PIL import Image
import os

# Path to your static folder
STATIC_DIR = "."
MAX_WIDTH = 800
MAX_HEIGHT = 600
QUALITY = 85  # WebP quality

# Supported image extensions
EXTENSIONS = (".jpg", ".png")

def convert_and_resize_images():
    for root, dirs, files in os.walk(STATIC_DIR):
        for file in files:
            if file.lower().endswith(EXTENSIONS):
                full_path = os.path.join(root, file)
                # Skip if already WebP
                if full_path.lower().endswith(".webp"):
                    continue

                try:
                    img = Image.open(full_path)
                    img.thumbnail((MAX_WIDTH, MAX_HEIGHT))  # Resize
                    webp_path = os.path.splitext(full_path)[0] + ".webp"
                    if os.path.exists(webp_path):
                        continue
                    
                    img.save(webp_path, "WEBP", quality=QUALITY, optimize=True)
                    print(f"Converted and resized: {file} -> {os.path.basename(webp_path)}")
                except Exception as e:
                    print(f"Error processing {file}: {e}")

if __name__ == "__main__":
    convert_and_resize_images()
