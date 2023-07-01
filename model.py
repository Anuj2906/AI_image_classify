from PIL import Image
import numpy as np
from tensorflow import keras
import os

def check(image):
    # Load the image

    # Preprocess the image
    image = image.resize((300, 300))  # Resize the image to the desired dimensions
    image = np.array(image)  # Convert the image to a numpy array
    image = image.astype('float32') / 255.0  # Normalize pixel values between 0 and 1

    # Expand dimensions and create a batch
    image = np.expand_dims(image, axis=0)

    model = keras.models.load_model('.\\image_classify.keras')

    # Make predictions
    predictions = model.predict(image)

    return predictions
