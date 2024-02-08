import os
# convert python dictinoary into markdown files

path = '/Users/maomao/Documents/GitHub/maomaocv.github.io/_posts/'
filename = input("Input file name (without extension):\n")
markdown_path = os.path.join(path, filename + ".markdown")

# Read the content of the markdown file
with open(markdown_path, 'r') as fp:
    content = fp.read()
content += "\n\n---\n"


# Write the modified content back to the file
with open(markdown_path, 'w') as fp:
    fp.write(content)

# Print the modified content
print(content)
