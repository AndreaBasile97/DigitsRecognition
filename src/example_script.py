import tensorflow as tf
from keras.preprocessing import image
from keras.models import load_model
import numpy as np

# Load the pre-trained model architecture
model = load_model("mnist_cnn_model.h5")

# Load the saved weights into the model
weights_path = "mnist_cnn_model_weights.h5"
model.load_weights(weights_path)

# Load and preprocess the new image
img_path = "fyPhv.jpg"
img = image.load_img(img_path, color_mode="grayscale", target_size=(28, 28))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array /= 255.0  # Normalize pixel values to be between 0 and 1

# Make predictions
predictions = model.predict(img_array)

# The predictions variable now contains the output of the model.
# You can print or use the predictions as needed for further processing.

print(predictions)
print(np.argmax(predictions))
