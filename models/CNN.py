# baseline cnn model for mnist
from numpy import mean
from numpy import std
from matplotlib import pyplot as plt
from keras.datasets import mnist
from sklearn.model_selection import KFold
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Dense
from keras.layers import Flatten
from keras.optimizers import SGD
import mlflow
from mlflow.keras import log_model
import dagshub
from dotenv import load_dotenv
import os
import numpy as np

# Load environment variables from the .env file
load_dotenv()

# Now you can access the environment variables using os.environ
dags_hub_username = os.environ.get("DAGS_HUB_USERNAME")

dagshub.init("DigitsRecognition", dags_hub_username, mlflow=True)
epochs = 10
batch_size = 32
shuffle = True
random_state = 1
learning_rate = 0.01
momentum = 0.9


# load train and test dataset
def load_dataset():
    # load dataset
    (trainX, trainY), (testX, testY) = mnist.load_data()
    # reshape dataset to have a single channel
    trainX = trainX.reshape((trainX.shape[0], 28, 28, 1))
    testX = testX.reshape((testX.shape[0], 28, 28, 1))
    # one hot encode target values
    trainY = to_categorical(trainY)
    testY = to_categorical(testY)
    return trainX, trainY, testX, testY


# scale pixels
def prep_pixels(train, test):
    # convert from integers to floats
    train_norm = train.astype("float32")
    test_norm = test.astype("float32")
    # normalize to range 0-1
    train_norm = train_norm / 255.0
    test_norm = test_norm / 255.0
    # return normalized images
    return train_norm, test_norm


# define cnn model
def define_model():
    model = Sequential()
    model.add(
        Conv2D(
            32,
            (3, 3),
            activation="relu",
            kernel_initializer="he_uniform",
            input_shape=(28, 28, 1),
        )
    )
    model.add(MaxPooling2D((2, 2)))
    model.add(Flatten())
    model.add(Dense(100, activation="relu", kernel_initializer="he_uniform"))
    model.add(Dense(10, activation="softmax"))
    # compile model
    opt = SGD(learning_rate=0.01, momentum=0.9)
    model.compile(optimizer=opt, loss="categorical_crossentropy", metrics=["accuracy"])
    log_model(model, "models")
    return model


# evaluate a model using k-fold cross-validation
def evaluate_model(dataX, dataY, n_folds=5):
    scores, histories = list(), list()
    # prepare cross validation
    kfold = KFold(n_folds, shuffle=shuffle, random_state=random_state)
    # enumerate splits
    mlflow.log_params(
        {
            "epochs": epochs,
            "batch_size": batch_size,
            "folds": n_folds,
            "shuffle": shuffle,
            "random_state": random_state,
        }
    )
    for train_ix, test_ix in kfold.split(dataX):
        # define model
        model = define_model()
        # select rows for train and test
        trainX, trainY, testX, testY = (
            dataX[train_ix],
            dataY[train_ix],
            dataX[test_ix],
            dataY[test_ix],
        )
        # fit model

        history = model.fit(
            trainX,
            trainY,
            epochs=epochs,
            batch_size=batch_size,
            validation_data=(testX, testY),
            verbose=0,
        )
        # evaluate model
        _, acc = model.evaluate(testX, testY, verbose=0)
        print("> %.3f" % (acc * 100.0))
        # stores scores
        scores.append(acc)
        histories.append(history)
    mlflow.log_metrics({"accuracy": scores[-1]})
    return scores, histories


# plot diagnostic learning curves
def summarize_diagnostics(histories):
    for i in range(len(histories)):
        # plot loss
        plt.subplot(2, 1, 1)
        plt.title("Cross Entropy Loss")
        plt.plot(histories[i].history["loss"], color="blue", label="train")
        plt.plot(histories[i].history["val_loss"], color="orange", label="test")
        # plot accuracy
        plt.subplot(2, 1, 2)
        plt.title("Classification Accuracy")
        plt.plot(histories[i].history["accuracy"], color="blue", label="train")
        plt.plot(histories[i].history["val_accuracy"], color="orange", label="test")
    plt.show()


# summarize model performance
def summarize_performance(scores):
    # print summary
    print(
        "Accuracy: mean=%.3f std=%.3f, n=%d"
        % (mean(scores) * 100, std(scores) * 100, len(scores))
    )
    # box and whisker plots of results
    plt.boxplot(scores)
    plt.show()


# run the test harness for evaluating a model


def run_test_harness():
    # Load normalized images
    trainX = np.load(os.path.join("data/processed", "train_norm.npy"))
    testX = np.load(os.path.join("data/processed", "test_norm.npy"))

    trainY = np.load(os.path.join("data/interim", "trainY.npy"))
    testY = np.load(os.path.join("data/interim", "testY.npy"))
    # evaluate model
    scores, histories = evaluate_model(trainX, trainY)
    # Save the trained model
    model = define_model()  # Define the model again to ensure consistency
    model_filename = "mnist_cnn_model.h5"
    model.save(model_filename)
    print("Model saved successfully as", model_filename)

    # Save learning curves
    summarize_diagnostics(histories)

    # Save metrics
    save_metrics(scores)

    # Summarize estimated performance
    summarize_performance(scores)


# Save the model to a file after training
def save_model(model, filename="model.h5"):
    model.save(filename)
    print("Model saved successfully as", filename)


# Save metrics to a CSV file
def save_metrics(scores, filename="metrics.csv"):
    import csv

    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Fold", "Accuracy"])
        for i, score in enumerate(scores, start=1):
            writer.writerow([i, score])
    print("Metrics saved successfully as", filename)


mlflow.start_run()

# entry point, run the test harness
run_test_harness()


mlflow.end_run()
