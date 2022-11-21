import os
from collections import OrderedDict
rootdir = '/Users/maomao/Documents/GitHub/maomaocv.github.io/img'

def store_path():
    path_ = {}
    SHOW_PATH = input("Press \"y\" to SHOW PATH: \n")
    if SHOW_PATH == "y":
        print(SHOW_PATH)
        for subdir, dirs, files in os.walk(rootdir):
            for file in files:
                f = os.path.join(subdir, file)
                if os.path.isfile(f):
                    print(f)
    else:
        print(SHOW_PATH, "\n>>> print and store file names only\n")
        for subdir, dirs, files in os.walk(rootdir):
            for file in files:
                f = os.path.join(subdir, file)
                tokens = f.split("/")
                path_[tokens[-1]] = ["Desciption: ", "Inserted_In: ", "Photo Credit: "]
                if os.path.isfile(f):
                    print(tokens[-1])
    return path_

def generator(dict):
    for key in dict:
        for i in range(len(dict[key])):
            print("dict[\"%s\"][%d] += \"\"" %(key, i))
        print("\n")
dict = store_path()
# dict[".jpg"] = ["Desciption: ", "Inserted_In: "]
# dict[".jpg"] = ["Desciption: ", "Inserted_In: "]
dict["01.jpg"][0] += "Selfie in light shirt"
dict["01.jpg"][1] += ""
dict["02.jpg"][0] += ""
dict["02.jpg"][1] += ""
dict["03.jpg"][0] += ""
dict["03.jpg"][1] += ""
dict["04.jpg"][0] += ""
dict["04.jpg"][1] += "404.html"
dict["05.jpg"][0] += ""
dict["05.jpg"][1] += ""
dict["06.jpg"][0] += ""
dict["06.jpg"][1] += ""
dict["07.jpg"][0] += ""
dict["07.jpg"][1] += ""

dict["09.jpg"][0] += "author portrait small"
dict["09.jpg"][1] += "_config.yml"
dict["10.jpg"][0] += ""
dict["10.jpg"][1] += ""

dict["galada-main-page.jpg"][0] += ""
dict["galada-main-page.jpg"][1] += ""
dict["galada-post.jpg"][0] += ""
dict["galada-post.jpg"][1] += ""
dict["nyc.jpg"][0] += ""
dict["nyc.jpg"][1] += ""
dict["nyc.png"][0] += ""
dict["nyc.png"][1] += ""

dict["03.jpg"][0] += "ZC"
dict["03.jpg"][1] += "/_pages/about.md"
dict["08.jpg"][0] += "Selfie in black shirt"
dict["08.jpg"][1] += "/_pages/styleguide.md"
dict["11.jpg"][0] += "Landscape"
dict["11.jpg"][1] += "/_pages/styleguide.md"
dict_sorted = OrderedDict(sorted(dict.items()))
for key in dict_sorted:
    print("\n", key, dict_sorted[key])
generator(dict_sorted)
print(dict_sorted)

# 2022 11 21

dict_latest = OrderedDict([('01.jpg', ['Desciption: ', 'Inserted_In: ']), ('02.jpg', ['Desciption: ', 'Inserted_In: ']), ('03.jpg', ['Desciption: ZC', 'Inserted_In: /_pages/about.md']), ('04.jpg', ['Desciption: ', 'Inserted_In: ']), ('05.jpg', ['Desciption: ', 'Inserted_In: ']), ('06.jpg', ['Desciption: ', 'Inserted_In: ']), ('07.jpg', ['Desciption: ', 'Inserted_In: ']), ('08.jpg', ['Desciption: Selfie in black shirt', 'Inserted_In: /_pages/styleguide.md']), ('09.jpg', ['Desciption: ', 'Inserted_In: ']), ('10.jpg', ['Desciption: ', 'Inserted_In: ']), ('11.jpg', ['Desciption: Landscape', 'Inserted_In: /_pages/styleguide.md']), ('galada-main-page.jpg', ['Desciption: ', 'Inserted_In: ']), ('galada-post.jpg', ['Desciption: ', 'Inserted_In: ']), ('nyc.jpg', ['Desciption: ', 'Inserted_In: ']), ('nyc.png', ['Desciption: ', 'Inserted_In: '])])

# print(dict_latest)
