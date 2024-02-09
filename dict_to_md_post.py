import os
# convert python dictinoary into markdown files
import datetime
import os
import time
# for timezone()
import pytz

# using datetime.now() to get current time
def get_time():
    current_time = datetime.datetime.now(pytz.timezone('Asia/Shanghai'))
    t = str(current_time)
    return t

def decapitalize(s, upper_rest = False):
    return ''.join([s[:1].lower(), (s[1:].upper() if upper_rest else s[1:])])

def post_name(time):
    # Input Title
    title_input = input("Please enter the title of the post: ")
    date = time[:10]
    tokens = decapitalize(title_input).split()
    title = date
    for i in range(len(tokens)):
        title += "-"
        title += tokens[i]
    title += ".markdown"
    path = '/Users/maomao/Documents/GitHub/maomaocv.github.io/_posts/'
    path += title
    # timezone
    tz = "+0800" # Beijing time +0800
    print("\n\n")
    print(title, "\n")
    # print("markdown template:\n")
    print("---\nlayout: post\ntitle:  ", title_input, "\ndate:   ", time[:19], tz)
    image = "00000.jpg"
    tags = "[Life]"
    print("image:  ", image, "\ntags:   ", tags, "\n---")

    # Post Content:
    content = ""
    content += "---\nlayout: post\ntitle:  " + title_input
    content += "\ndate:   " + time[:19]+ tz
    content += "\nimage:  " + image + "\ntags:   " + tags + "\n---\n"    # print(content)
    fp = open(path, 'w')
    fp.write(content)
    fp.close()

def recent_post(time):
    tags = input("Enter tags in the format [tag1, tag2]:\n")
    text = input("Enter text:\n")
    title_input = "recent updates"
    date = time[:10]
    tokens = title_input.split()
    title = date
    for i in range(len(tokens)):
        title += "-"
        title += tokens[i]
    title += ".markdown"
    path = '/Users/maomao/Documents/GitHub/maomaocv.github.io/_posts/'
    path += title
    # timezone
    tz = "+0800" # Beijing time +0800
    print("\n\n")
    print(title, "\n")
    # print("markdown template:\n")
    print("---\nlayout: post\ntitle:  ", title_input, "\ndate:   ", time[:19], tz)
    image = "00000.jpg"
    # tags = "[Commonplace, Life]"
    print("image:  ", image, "\ntags:   ", tags, "\n---")

    # Post Content:
    content = ""
    content += "---\nlayout: post\ntitle:  " + "Recent Updates"
    content += "\ndate:   " + time[:19]+ tz
    content += "\nimage:  " + image + "\ntags:   " + tags + "\n---\n"
    # content += "Web Application + Researches"
    content += text
    fp = open(path, 'w')
    fp.write(content)
    fp.close()
recent_post(get_time())
# post_name(get_time())

# path = '/Users/maomao/Documents/GitHub/maomaocv.github.io/_posts/'
# filename = input("Input file name (without extension):\n")
# markdown_path = os.path.join(path, filename + ".markdown")

# # Read the content of the markdown file
# with open(markdown_path, 'r') as fp:
#     content = fp.read()
# content += "\n\n---\n"


# # Write the modified content back to the file
# with open(markdown_path, 'w') as fp:
#     fp.write(content)

# # Print the modified content
# print(content)
