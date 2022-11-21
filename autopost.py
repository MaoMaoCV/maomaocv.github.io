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
    temp = input("Please enter the title of the post: ")
    de_temp = decapitalize(temp)
    # print(time)
    date = time[:10]
    # t_ = time[12:19]
    # _t = t_.split(':')
    tokens = de_temp.split()
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
    content += "\ndate:   " + time[:19]+ tz
    content += "\nimage:  " + image + "\ntags:   " + tags + "\n---\n"    # print(content)
    fp = open(path, 'w')
    fp.write(content)
    fp.close()

def recent_post(time):
    temp = "recent updates"
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
    image = "01.jpg"
    tags = "[Commonplace, Life]"
    print("image:  ", image, "\ntags:   ", tags, "\n---")

    # Post Content:
    content = ""
    content += "---\nlayout: post\ntitle:  " + "Recent Updates"
    content += "\ndate:   " + time[:19]+ tz
    content += "\nimage:  " + image + "\ntags:   " + tags + "\n---\n"
    content += "Web Application + Researches"
    fp = open(path, 'w')
    fp.write(content)
    fp.close()

post_name(get_time())

time.sleep(2)

recent_post(get_time())


'''
---
layout: post
title:  Recent Updates
date:   2022-11-21 00:05:00 +0800
image:  01.jpg
tags:   [Commonplace]
---

Web Application

Researches

GRE
'''
