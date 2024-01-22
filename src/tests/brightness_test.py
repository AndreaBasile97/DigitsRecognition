import tensorflow as tf
from keras.datasets import mnist
from keras.preprocessing import image
from keras.models import load_model
import numpy as np
import pytest

# Load the pre-trained model architecture
model = load_model("mnist_cnn_model.h5")

# Load the saved weights into the model
weights_path = "mnist_cnn_model_weights.h5"
model.load_weights(weights_path)

# Load the first, tenth, and ninth images from the MNIST dataset
(_, _), (x_test, _) = mnist.load_data()
indices = [4, 9, 8]  # Indices of images to process
images = x_test[indices]


# Common function to preprocess image
def preprocess_image(img):
    img = np.expand_dims(img, axis=-1)
    img = image.array_to_img(img, data_format="channels_last", scale=False)
    img = img.resize((28, 28))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    return img_array


# Common function to predict and print results
def predict_and_print(img_array, brightness=False):
    if brightness:
        grey = (img_array * 255).astype(np.uint8)
        mask = (255 - grey) < 10
        img_array = np.where(mask, 255, grey + 10).astype(np.float32) / 255.0

    predictions = model.predict(img_array)
    print("\nPredictions:")
    print(predictions)
    print("Predicted digit:", np.argmax(predictions))


# Pytest test function
@pytest.mark.parametrize("img_index", [0, 1, 2])
def test_brightness_adjustment(img_index):
    img_array = preprocess_image(images[img_index])

    # Predict without brightness adjustment
    predict_and_print(img_array)

    # Predict with brightness adjustment
    predict_and_print(img_array, brightness=True)
