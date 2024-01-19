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


@app.post("/model")
async def predict_image(item: UploadFile):
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


@app.get("/models")
async def get_last_accuracy():
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
