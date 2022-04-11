import sys
from PIL import Image
from pytesseract import image_to_string

def img_to_str(name_image):
    return image_to_string(Image.open(name_image)).rstrip()

