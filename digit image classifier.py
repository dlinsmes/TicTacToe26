import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image
import random
import tensorflow as tf

imDirectory = "Digits"
data = []

for imFile in os.listdir(imDirectory):

    #get what number the image is of
    classification = int(imFile[len(imFile)-5])

    #read pixel data, scale [0,255] to [0,1]
    img_array = np.array(Image.open(os.path.join(imDirectory, imFile)))
    img_array = img_array / 255

    data.append([img_array, classification])

    # print(classification)
    # plt.imshow(img_array, cmap="gray")
    # plt.show()
    # print(img_array)
    # print(img_array)
    # break


random.shuffle(data)

# for sample in data[:10]:
#     print(sample[1])

imData = []
imLabels = []
for image, label in data:
    imData.append(image)
    imLabels.append(label)

imData = np.array(imData)
imLabels = np.array(imLabels)

model = tf.keras.models.load_model('num_reader.keras')
predictions = model.predict(imData)

# print(len(predictions), "predictions")
# print(predictions[0])
# print("prediction", np.argmax(predictions[0]))
# print("real", imLabels[0])
# plt.imshow(imData[0], cmap="gray")
# plt.show()