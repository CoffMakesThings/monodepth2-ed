from PIL import Image
import os
import sys

dirStrings = ["cafe_0001a", "cafe_0001b", "cafe_0001c"]

for dirString in dirStrings:
    counter = 0
    os.makedirs("E:/DL Data/Converted/{}/Depth".format(dirString))
    for path in os.listdir("E:/DL Data/{}/".format(dirString)):
        if (path.endswith('pgm')):
            # print(path)
            im = Image.open("E:/DL Data/{}/{}".format(dirString, path))
            im.save("E:/DL Data/Converted/{}/Depth/{}.png".format(dirString, counter))
            sys.stdout.write("{} converted\n".format(path))
            sys.stdout.flush()
            counter += 1

    os.makedirs("E:/DL Data/Converted/{}/Main".format(dirString))
    counter = 0
    for path in os.listdir("E:/DL Data/{}/".format(dirString)):
        if (path.endswith('ppm')):
            # print(path)
            im = Image.open("E:/DL Data/{}/{}".format(dirString, path))
            im.save("E:/DL Data/Converted/{}/Main/{}.png".format(dirString, counter))
            sys.stdout.write("{} converted\n".format(path))
            sys.stdout.flush()
            counter += 1