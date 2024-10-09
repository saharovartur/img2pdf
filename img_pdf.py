import os

import img2pdf
from PIL import Image


# Путь до вашего фото
img_path = r"C:\Users\YourUserName\Desktop\я.jpg"

# Путь для файла pdf
# Я заранее создал папку me на рабочем столе
pdf_path = r"C:\Users\YourUserName\Desktop\me\file.pdf"

try:
    # Открываем фотку
    image = Image.open(img_path)

    # конвертировать в  PDF
    pdf_bytes = img2pdf.convert(image.filename)

    # Opening or creating pdf file
    with open(pdf_path, "wb") as file:
        # Writing pdf files with chunks
        file.write(pdf_bytes)

    print("Successfully made pdf file")

except FileNotFoundError:
    print(f"The image file {img_path} does not exist.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    if hasattr(image, 'close'):
        image.close()
