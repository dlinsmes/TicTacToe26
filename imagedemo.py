#pycharm menu - settings - python - interpretter
#-install pillow

from PIL import Image

#read image file
im = Image.open("duck.jpg")

#display image
im.show()

#tuple - set of values (like an array)
print("size:", im.size)

#tuples can be indexed like arrays
#width is the number of columns - think of as x
print("width:", im.size[0])

#load image as a pixel array
pixels = im.load()

#get value of the pixel at 0,0
#color images have 3 vals per pixel - R G B
print(pixels[0, 0])

#pixel at the bottom right
#width and height are like an array length
#where indexing is exclusive of those values
print(pixels[899, 1199])

#out of bounds when flipped
# print(pixels[1199, 899])

#blue value at the bottom right pixel
#need to index the tuple of the RGB value
print(pixels[899, 1199][2])

#save each rgb value separately
r, g, b = pixels[0,0]
print(r)
print(g)
print(b)

#calculate the vertical midpoint
vMid = im.size[1] / 2
print(vMid)

#argument for crop is a tuple of 4 values:
#-left, top, right, bottom
#(clockwise starting from left)
cropped = im.crop((0, 0, im.size[0], vMid))
cropped.show()

#can use crop to add space around an image
cropped = im.crop((-50, 0, im.size[0]+50, vMid))
cropped.show()

#split the full color image into individual RGB channels
red, green, blue = im.split()

#the individual channels are interpreted as b+w photos
red.show()
green.show()
blue.show()

redPx = red.load()
#not a tuple bc this is a single color channel
print(redPx[0,0])

#merge the individual color channels into a single color image
merged = Image.merge("RGB", (red, green, red))
merged.show()