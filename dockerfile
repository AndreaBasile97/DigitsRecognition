# Use a base image with Python and TensorFlow
FROM tensorflow/tensorflow:latest

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

RUN python -m venv /opt/venv && \
    . /opt/venv/bin/activate && \
    pip install --no-cache-dir -r requirements.txt

# Make sure the virtual environment is activated each time the container runs
ENV PATH="/opt/venv/bin:$PATH"

# Copy the application code into the container
COPY . /app

# Expose port 80 for incoming connections
EXPOSE 80

# Command to run the FastAPI application using uvicorn
CMD ["uvicorn", "src.digits_recognition_api:app", "--host", "0.0.0.0", "--port", "3000"]
