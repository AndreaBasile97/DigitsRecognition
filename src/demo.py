import gradio as gr
import requests

# Define the Gradio input component
input_component = gr.File(label="Upload Image", type="file")

# Define the Gradio output component
output_component = gr.Textbox(text="Predicted Label", type="text")


# Define the Gradio function that uses the FastAPI endpoint
def predict_image(file):
    response = requests.post(
        "http://127.0.0.1:3000/predict", files={"item": (file.name, file.read())}
    )
    result = response.json()
    return result["predicted_label"]


# Create the Gradio interface
iface = gr.Interface(
    fn=predict_image, inputs=input_component, outputs=output_component, live=True
)

# # Launch the Gradio interface
# iface.launch()
