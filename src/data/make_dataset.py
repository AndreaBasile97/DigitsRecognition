from keras.utils import to_categorical
import numpy as np
import os
from keras.datasets import mnist


interim_folder = "data/interim"
processed_folder = "data/processed"


def load_mnist_data():
    (trainX, trainY), (testX, testY) = mnist.load_data()
    print(trainX.shape)
    print(testX.shape)
    return (trainX, trainY), (testX, testY)


def intermediate_process(trainX, testX, trainY, testY):
    # reshape dataset to have a single channel
    trainX = trainX.reshape((trainX.shape[0], 28, 28, 1))
    testX = testX.reshape((testX.shape[0], 28, 28, 1))
    # one hot encode target values
    trainY = to_categorical(trainY)
    testY = to_categorical(testY)
    # Save artifacts
    np.save(os.path.join(interim_folder, "trainX.npy"), trainX)
    np.save(os.path.join(interim_folder, "testX.npy"), testX)
    np.save(os.path.join(interim_folder, "trainY.npy"), trainY)
    np.save(os.path.join(interim_folder, "testY.npy"), testY)

    return trainX, trainY, testX, testY


# scale pixels
def prep_pixels(train, test):
    # convert from integers to floats
    train_norm = train.astype("float32")
    test_norm = test.astype("float32")
    # normalize to range 0-1
    train_norm = train_norm / 255.0
    test_norm = test_norm / 255.0
    # Save normalized images
    np.save(os.path.join(processed_folder, "train_norm.npy"), train_norm)
    np.save(os.path.join(processed_folder, "test_norm.npy"), test_norm)

    return train_norm, test_norm


(trainX, trainY), (testX, testY) = load_mnist_data()
trainX, testX, trainY, testY = intermediate_process(trainX, testX, trainY, testY)
preprocessed_dataset = prep_pixels(trainX, testX)
