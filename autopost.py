import datetime
import os
# for timezone()
import pytz

# using now() to get current time
current_time = datetime.datetime.now(pytz.timezone('Asia/Shanghai'))
t = str(current_time)

def post_name(time):
    temp = input("Please enter the title of the post: ")
    # print(time)
    date = time[:10]
    # t_ = time[12:19]
    # _t = t_.split(':')
    tokens = temp.split()
    title = date
    for i in range(len(tokens)):
        title += "-"
        title += tokens[i]
    # for i in range(len(_t)):
    #     t += _t[i]
    #     t += "-"
    title += ".markdown"
    path = '/Users/maomao/Documents/GitHub/maomaocv.github.io/_posts/'
    path += title
    # timezone
    tz = "+0800" # Beijing time +0800
    # print("auto-generated-title:\n")
    print("\n\n")
    print(title, "\n")
    # print("markdown template:\n")
    print("---\nlayout: post\ntitle:  ", temp, "\ndate:   ", time[:19], tz)
    image = "05.jpg"
    tags = "Life"
    print("image:  ", image, "\ntags:   ", tags, "\n---")

    # Post Content:
    content = ""
    content += "---\nlayout: post\ntitle:  " + temp
    content += "\ndate:   " + time[:19]+ tz + "\nimage:  " + image + "\ntags:   " + tags + "\n---"
    # print(content)
    fp = open(path, 'w')
    fp.write(content)
    fp.close()


post_name(t)
# print(post_name(t))


'''
---
layout: post
title:  The path to self-perfection
date:   2018-08-23 16:03:30 +0800
image:  05.jpg
tags:   Life
---
'''
