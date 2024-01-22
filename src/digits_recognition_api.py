from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from PIL import Image
import numpy as np
from keras.models import load_model
from keras.preprocessing import image
from io import BytesIO
import pandas as pd

app = FastAPI()

# Load the saved model
loaded_model = load_model("mnist_cnn_model.h5")
# Load the saved weights into the model
weights_path = "mnist_cnn_model_weights.h5"
loaded_model.load_weights(weights_path)


@app.post("/predict")
async def predict_image(item: UploadFile):
    "The model is trained to recognize handwritten digits in images and the image size must be 28x28 pixels. The dataset used to train this model, the MNIST dataset, is comprised by images of handwritten digits from 0 to 9, therefore this model will only recognize separated units."
    try:
        # Read the image file directly from the UploadFile
        contents = item.file.read()

        # Load the image from bytes
        img = Image.open(BytesIO(contents)).convert("L").resize((28, 28))

        # Convert the image to a NumPy array and normalize pixel values
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.0

        # Make predictions using the loaded model
        predictions = loaded_model.predict(img_array)
        print(predictions)
        predicted_label = int(np.argmax(predictions[0]))

        # Define the class labels (0 to 9)
        class_labels = list(map(int, range(10)))

        # Return the predicted label
        return JSONResponse(
            content={"predicted_label": predicted_label, "class_labels": class_labels}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/model_metrics")
async def get_last_accuracy():
    "The output of this step is the main metric to evaluate the efficacy of the model, which is the accuracy, reported as a percentage value."
    # Read the CSV file into a Pandas DataFrame
    metrics_df = pd.read_csv("metrics.csv")
    try:
        # Get the last row (which corresponds to the last fold) from the DataFrame
        last_row = metrics_df.iloc[-1]

        # Extract the accuracy value from the last row
        last_accuracy = last_row["Accuracy"]

        return {"last_accuracy": last_accuracy}

    except Exception as e:
        return {"error": str(e)}
