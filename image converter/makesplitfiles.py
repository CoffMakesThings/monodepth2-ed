from PIL import Image
import os

dirStrings = ["cafe_0001a", "cafe_0001b", "cafe_0001c"]
rootDirTemplate = "E:/DL Data/Converted/{}/Main"
line1Template = "converted/{}"

str = ""

for dirString in dirStrings:
    for path in os.listdir(rootDirTemplate.format(dirString)):
        line1 = line1Template.format(dirString)
        # print(path)
        str += "{} {} {}\n".format(line1, path.split('.')[0], "r")

f = open("split.txt", "a")
f.write(str)
f.close()