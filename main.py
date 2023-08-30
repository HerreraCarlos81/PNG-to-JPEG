from PIL import Image
import glob
from pathlib import Path
import os
from datetime import date

def find_files():
    # Find and return all files within the ./pngs directory
    png_files = Path('./pngs').rglob('*.png')
    return png_files



def convert_files():
    png_files = find_files()
    for file in png_files:
        # Convert png to jpeg
        img = Image.open(file)
        jpeg_file = f"./jpegs/{date.today().strftime('%Y%m%d')}_{file.stem}.jpeg"
        img.save(jpeg_file, "JPEG")
        
        # Delete png file
        os.remove(file)


# Run the conversion when the script is called
if __name__ == "__main__":
    convert_files()
