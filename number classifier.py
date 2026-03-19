import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

model = tf.keras.models.load_model("num_reader.keras")

mnist = tf.keras.datasets.mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

predictions = model.predict(test_images)
print(predictions)

#10000 test images
print(len(predictions))

#any given row has length 10 where the largest value is at the position
#of the guessed number
print(predictions[0])

print("guess", np.argmax(predictions[0]))
print("real", test_labels[0])
plt.imshow(test_images[0], cmap="gray")
plt.show()

#calculate the accuracy percentage of the predictions of the test set
#for the first 5 incorrect classifications,
# print the prediction, actual, and show the image