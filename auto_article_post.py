from PIL import Image
import os
import shutil

date = "2021-06-09"
title_name = "Linear Transformers Are Secretly Fast Weight Programmers"
URL = "https://arxiv.org/pdf/2102.11174.pdf"

def rename_and_move(new_name):
    src_dir = "/Users/maomao/Desktop"
    dest_dir = "/Users/maomao/Documents/GitHub/maomaocv.github.io/img"
    
    files = [os.path.join(src_dir, f) for f in os.listdir(src_dir) if os.path.isfile(os.path.join(src_dir, f))]

    latest_file = max(files, key=os.path.getctime)

    # Rename and move the file
    new_file_path = os.path.join(dest_dir, new_name)
    shutil.move(latest_file, new_file_path)

def auto_post(date, title, markdown_name, img_name, URL):
    path = '/Users/maomao/Documents/GitHub/maomaocv.github.io/_posts/'
    path += markdown_name
    # timezone
    timezone = " 16:03:30 +0800" # Beijing time +0800
    print("\n\n")
    print(title, "\n")
    # print("markdown template:\n")
    print("---\nlayout: post\ntitle:  ", title, "\ndate:   ", date, timezone)
    tags = "[AI, arXiv]"
    print("image:  ", img_name, "\ntags:   ", tags, "\n---")

    # Post Content:
    content = ""
    content += "---\nlayout: post\ntitle:  " + title
    content += "\ndate:   " + date + timezone
    content += "\nimage:  " + img_name + "\ntags:   " + tags + "\n---\n"
    content += f"arXiv V1: [{title}]({URL})"
    fp = open(path, 'w')
    fp.write(content)
    fp.close()

def make_title(title_string):
    user_input = title_string
    processed_string = user_input.lower().replace(" ", "-")
    title = ' '.join(word.capitalize() for word in user_input.split())
    title += '.markdown'
    return processed_string, title

img_name = f"{date}.jpg"
rename_and_move(img_name)
img_name = f"{date}s.jpg"
img = Image.open(f"/Users/maomao/Documents/GitHub/maomaocv.github.io/img/{date}.jpg")
max_side = max(img.size)
canvas = Image.new('RGB', (max_side, max_side), 'white')

x_offset = (canvas.width - img.width) // 2
y_offset = (canvas.height - img.height) // 2
canvas.paste(img, (x_offset, y_offset))
canvas.save(f"/Users/maomao/Documents/GitHub/maomaocv.github.io/img/{date}s.jpg")
markdown, article_title = make_title(title_name)
print("image saved as", date, "s.jpg")

markdown_name = f"{date}-{markdown}"
auto_post(date, article_title, markdown_name, img_name, URL)
