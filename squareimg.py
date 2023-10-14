from PIL import Image

name = "2023-09-13"

img = Image.open(f"/Users/maomao/Documents/GitHub/maomaocv.github.io/img/{name}.jpg")

# Determine the longer side
max_side = max(img.size)

# Create a white square canvas
canvas = Image.new('RGB', (max_side, max_side), 'white')

# Calculate the position to paste the image onto the canvas
x_offset = (canvas.width - img.width) // 2
y_offset = (canvas.height - img.height) // 2
canvas.paste(img, (x_offset, y_offset))
canvas.save(f"/Users/maomao/Documents/GitHub/maomaocv.github.io/img/{name}s.jpg")

