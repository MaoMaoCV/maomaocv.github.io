import pytesseract
from PIL import Image

name = "2023-09-27"

image = Image.open(f"/Users/maomao/Documents/GitHub/maomaocv.github.io/img/{name}.jpg")

extracted_text = pytesseract.image_to_string(image)

# Split the extracted text into lines to retrieve individual names
names = extracted_text.split('\n')
names = [name.strip() for name in names if name.strip()]

names