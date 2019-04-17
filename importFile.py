# A method to read various kinds of files for easy import. Working on adding other types, such as csv.

import cv2
import matplotlib.pyplot as plt


def importfile(file):
    if str(file).__contains__("txt"):
        importedfile = open(file, "r")
        importedfile = importedfile.read()

    if str(file).__contains__("png") or str(file).__contains__("jpg"):
        import cv2
        importedfile = cv2.imread(file, 1)

    return importedfile


# examples:
# opened = importfile('cache/Magnitude_favoriteImage.png')
# imgplot = plt.imshow(opened)
# plt.show()
#
# openedtxt = importfile('cache/token.txt')
# print(openedtxt)
