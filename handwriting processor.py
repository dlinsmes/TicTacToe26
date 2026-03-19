from PIL import Image, ImageOps
import os

directory = "Handwriting Sheets"
for filename in os.listdir(directory):
    # print(filename)

    im = Image.open(os.path.join(directory, filename))
    im = ImageOps.grayscale(im)

    px = im.load()

    #take the image of the 7 x 10 sheet and cut up each individual grid box
    #then preprocess according to mnist standard (see slides)