from PIL import Image
import os
import shutil

INPUT_MODE = True # INPUT_MODE = False for manual inputs

if(INPUT_MODE):
    date = input("Enter date of the article: (<EXAMPLE INPUT> = \"2023-12-31\") \n")
    title_name = input("Enter name of the article:\n")
    URL = input("Enter URL of the article: (<EXAMPLE INPUT> = \"https://arxiv.org/pdf/1234.56789.pdf \")\n")
    cites = input("Enter citaion in k: (<YOUR INPUT> round your input to one digit after the decimal)\n")
else:
    date = "2021-06-09"
    title_name = "Linear Transformers Are Secretly Fast Weight Programmers"
    URL = "https://arxiv.org/pdf/2102.11174.pdf"

def find_latest_file(src_dir, allowed_extensions):
    files = [os.path.join(src_dir, f) for f in os.listdir(src_dir) if os.path.isfile(os.path.join(src_dir, f))]
    # Filter files by allowed extensions (e.g., png and jpg)
    filtered_files = [f for f in files if f.lower().endswith(allowed_extensions)]
    if not filtered_files:
        return None
    # Find the latest file among the filtered files
    latest_file = max(filtered_files, key=os.path.getctime)
    return latest_file

def rename_and_move(new_name):
    src_dir = "/Users/maomao/Desktop"
    dest_dir = "/Users/maomao/Documents/GitHub/maomaocv.github.io/img"
    allowed_extensions = ('.png', '.jpg')

    latest_file = find_latest_file(src_dir, allowed_extensions)

    if latest_file is None:
        print("No files with allowed extensions found in the source directory.")
        return
    # Rename and move the file
    new_file_path = os.path.join(dest_dir, new_name)
    shutil.move(latest_file, new_file_path)

def auto_post(date, post_title, article_title, markdown_name, img_name, URL):
    path = '/Users/maomao/Documents/GitHub/maomaocv.github.io/_posts/'
    path += markdown_name
    # timezone
    timezone = " 16:03:30 +0800" # Beijing time +0800
    print("\n\n")
    print(article_title, "\n")
    # print("markdown template:\n")
    print("---\nlayout: post\ntitle:  ", post_title, "\ndate:   ", date, timezone)
    tags = f"[Transformer, AI, arXiv, ~{cites}k Citations]"
    print("image:  ", img_name, "\ntags:   ", tags, "\n---")
    print(f"arXiv V1: [{article_title}]({URL})")

    # Post Content:
    content = ""
    content += "---\nlayout: post\ntitle:  " + post_title
    content += "\ndate:   " + date + timezone
    content += "\nimage:  " + img_name + "\ntags:   " + tags + "\n---\n\n"
    raw_URL = URL.replace("/pdf/", "/abs/").replace(".pdf", "")
    content += f"[arXiv]({raw_URL}) V1: [{article_title}]({URL})"
    fp = open(path, 'w')
    fp.write(content)
    fp.close()

def capitalize_words(title):
    stop_words = ["the", "and", "in", "of", "to", "a", "an", "for", "on", "with", "as", "by", "at", "but", "or", "nor", "so", "yet"]
    words = title.split()
    processed_words = []
    for word in words:
        if word.lower() in stop_words:
            processed_words.append(word.lower())
        else:
            processed_words.append(word.capitalize())

    processed_string = ' '.join(processed_words)
    return processed_string

def make_title(title_string):
    user_input = title_string
    title = capitalize_words(title_string)
    post_title = title.replace(":", " -")

    markdown_name = user_input.lower().replace(" ", "-")
    while(markdown_name[-1] == '-'):
        markdown_name = markdown_name[:-1]
    markdown_name = markdown_name.replace(":", "")
    jpg_name = markdown_name
    markdown_name += '.markdown'
    return markdown_name, post_title, jpg_name




markdown, post_title, jpg_name = make_title(title_name)
img_name = f"{date}-{jpg_name}.jpg"
rename_and_move(img_name)
img_name = f"{date}-{jpg_name}_squared.jpg"
img = Image.open(f"/Users/maomao/Documents/GitHub/maomaocv.github.io/img/{date}-{jpg_name}.jpg")
max_side = max(img.size)
canvas = Image.new('RGB', (max_side, max_side), 'white')
x_offset = (canvas.width - img.width) // 2
y_offset = (canvas.height - img.height) // 2
canvas.paste(img, (x_offset, y_offset))
canvas.save(f"/Users/maomao/Documents/GitHub/maomaocv.github.io/img/{date}-{jpg_name}_squared.jpg")
print("image saved as", img_name)
markdown_name = f"{date}-{markdown}"
print(markdown_name)
auto_post(date, post_title, title_name, markdown_name, img_name, URL)
