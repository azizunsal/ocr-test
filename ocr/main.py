import tesserocr
from PIL import Image

print(tesserocr.tesseract_version())
print(tesserocr.get_languages())

image = Image.open('IMG_5430.jpg')

print(tesserocr.image_to_text(image))
