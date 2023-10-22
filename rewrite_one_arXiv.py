import os

path = '/Users/maomao/Documents/GitHub/maomaocv.github.io/_posts/'
filename = input("Input file name (without extension):\n")
markdown_path = os.path.join(path, filename + ".markdown")

# Read the content of the markdown file
with open(markdown_path, 'r') as fp:
    content = fp.read()

# Find and extract the URL
start_index = content.find("https://arxiv.org/pdf/")
if start_index != -1:
    end_index = content.find(".pdf", start_index)
    if end_index != -1: 
        URL = content[start_index:end_index + 4]
        raw_URL = URL.replace("/pdf/", "/abs/").replace(".pdf", "")

# Replace "arXiv" with the modified URL
content = content.replace("arXiv V", f"[arXiv]({raw_URL}) V")
content += "\n\n---\n[NASA ADS](https) - \n[Google Scholar](https) - \n[Semantic Scholar](https)\n\n{% highlight markdown %}\n\n{% endhighlight %}"
content += "\n\n---\n"


# Write the modified content back to the file
with open(markdown_path, 'w') as fp:
    fp.write(content)

# Print the modified content
print(content)


# from PIL import Image
# import os
# import shutil

# path = '/Users/maomao/Documents/GitHub/maomaocv.github.io/_posts/'
# path += input("Input file name:\n")
# path += ".markdown"

# ### YOUR CODE GOES HERE

# fp = open(path, 'w')
# fp.write(content)
# fp.close()

# load file to a string variable named content from path
# find "https://arxiv.org/pdf/<some number here>.pdf"
# store it as a string varaible named URL
# then add this line:
# raw_URL = URL.replace("/pdf/", "/abs/").replace(".pdf", "")
# look for "arXiv " in the file and replace it with "[arXiv]({<raw_URL>}) "

# my file is like this:
# ---
# layout: post
# title:  Self-taught Optimizer (STOP) - Recursively Self-Improving Code Generation
# date:   2023-10-03 16:03:30 +0800
# image:  2023-10-03s-Zelikman.jpg
# tags:   [Self-Improving, Meta Learning, GPT4, Transformer, AI, arXiv]
# ---

# arXiv V1: [SELF-TAUGHT OPTIMIZER (STOP): RECURSIVELY SELF-IMPROVING CODE GENERATION](https://arxiv.org/pdf/2310.02304.pdf)



