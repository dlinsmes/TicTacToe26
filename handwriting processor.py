from PIL import Image, ImageOps
import os

directory = "Handwriting Sheets"
for filename in os.listdir(directory):
    # print(filename)

    im = Image.open(os.path.join(directory, filename))
    im = ImageOps.grayscale(im)

    px = im.load()

    #crop out the border white

    for row in range(7):
        for col in range(10):

            #follow the preprocessing steps

            #don't use - just for sample black images
            numIm = Image.new("L", [28, 28])

            #save the individual preprocessed digit image to the Digits directory
            # print(filename[11:14]) #file number: 118, 199, 120
            imFileName = filename[11:14] + "-r" + str(row) + "-c" + str(col) + ".png"
            # print(imFileName)

            numIm.save(f"Digits/"+imFileName, "PNG")



    #take the image of the 7 x 10 sheet and cut up each individual grid box
    #then preprocess according to mnist standard (see slides)

    #for loop syntax for setting an initial value and increment
    #starting value is -5, condition is < 10, increment is += 2
    # for i in range (-5, 10, 2):