from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from PIL import Image
import numpy as np
from keras.models import load_model
from keras.preprocessing import image
from io import BytesIO
import pandas as pd
import gradio as gr
import requests


app = FastAPI()

# Load the saved model
loaded_model = load_model("mnist_cnn_model.h5")
# Load the saved weights into the model
weights_path = "mnist_cnn_model_weights.h5"
loaded_model.load_weights(weights_path)

ALLOWED_EXTENSIONS = {"jpg", "jpeg"}


def allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def make_prediction(input_data: bytes | Image.Image):
    try:
        if isinstance(input_data, bytes):
            # Load the image from bytes
            img = Image.open(BytesIO(input_data)).convert("L").resize((28, 28))
        elif isinstance(input_data, Image.Image):
            img = input_data.convert("L").resize((28, 28))
        else:
            raise ValueError("Input must be either bytes or a file path")

        # Convert the image to a NumPy array and normalize pixel values
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.0

        # Make predictions using the loaded model
        predictions = loaded_model.predict(img_array)
        print(predictions)
        predicted_label = int(np.argmax(predictions[0]))

        # Return the predicted label
        return predicted_label
    except Exception as e:
        print(e)


@app.post("/predict")
async def predict_image(item: UploadFile):
    "The model is trained to recognize handwritten digits in images, which must not be in .PNG, 
    and the image size must be 28x28 pixels. The dataset used to train this model, the MNIST dataset,
    is comprised by images of handwritten digits from 0 to 9, therefore this model will only recognize separated units."
    try:
        # Check if the file has an allowed extension
        if not allowed_file(item.filename):
            raise HTTPException(status_code=400, detail="Only JPEG files are allowed")
        # Read the image file directly from the UploadFile
        contents = item.file.read()
        # Define the class labels (0 to 9)
        class_labels = list(map(int, range(10)))
        predicted_label = make_prediction(contents)
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


# Create the Gradio interface
iface = gr.Interface(
    fn=make_prediction, inputs=gr.Image(type="pil"), outputs="text", live=True
)

app = gr.mount_gradio_app(app, iface, path="/gradio")
