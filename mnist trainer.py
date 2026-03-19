import tensorflow as tf
import matplotlib.pyplot as plt

#dataset of images of handwritten digits
mnist = tf.keras.datasets.mnist

#load the training and test images/labels (classifications)
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

print(len(train_images), len(test_images))

# plt.imshow(train_images[0], cmap="gray")
# plt.show()
# print(train_labels[0])

# print(train_images[0])

#pixel values are [0,255], scale the values to [0,1]
train_images = train_images / 255.0
test_images = test_images / 255.0

# print(train_images[0])

model = tf.keras.models.Sequential()

#each image is 28 x 28 pixels - transform each one to be 1 x 784
model.add(tf.keras.layers.Flatten())

#hidden layers
model.add(tf.keras.layers.Dense(128, activation="relu"))
model.add(tf.keras.layers.Dense(128, activation="relu"))

#number of classifications
model.add(tf.keras.layers.Dense(10, activation="softmax"))

model.compile(optimizer = "adam", loss = "sparse_categorical_crossentropy", metrics = ["accuracy"])

#train the model using the training images and labels, epochs is the number of passes
model.fit(train_images, train_labels, epochs = 5)

#save the model so we don't need to retrain every time
model.save("num_reader.keras")
