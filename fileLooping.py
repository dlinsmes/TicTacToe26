from PIL import Image

#start i at 1 and go up to 7 (exclusive)
for i in range (1, 7):

    #generate file name
    file = "im" + str(i) + ".jpg"
    print(file)

    #look in the image alignment subfolder
    im = Image.open("image alignment/" + file)
    im.show()