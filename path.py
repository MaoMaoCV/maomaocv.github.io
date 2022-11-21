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
                path_[tokens[-1]] = ["Desciption: ", "Inserted_In: "]
                if os.path.isfile(f):
                    print(tokens[-1])
    return path_

def generator(dict):
    for key in dict:
        for i in range(len(dict[key])):
            print("dict[\"%s\"][%d] += \"\"" %(key, i))
dict = store_path()
# dict[".jpg"] = ["Desciption: ", "Inserted_In: "]
# dict[".jpg"] = ["Desciption: ", "Inserted_In: "]

dict["03.jpg"][0] += "ZC"
dict["03.jpg"][1] += "Inserted_In: /_pages/styleguide.md"
dict["08.jpg"] = ["Selfie in black shirt", "Inserted_In: /_pages/about.md"]
dict["11.jpg"] = ["Desciption: Landscape", "Inserted_In: /_pages/styleguide.md"]
dict_sorted = OrderedDict(sorted(dict.items()))
for key in dict_sorted:
    print("\n", key, dict_sorted[key])
generator(dict_sorted)
