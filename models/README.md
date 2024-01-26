# Model Card

## Model Details

- **Person or Organization Developing Model:** Basile Andrea, Di Lago Maria Grazia, Pizzillo Valentina, Saltarelli Silvia
- **Model Date:** 11/01/2024
- **Model Version:** 1.0
- **Model Type:** CNN
- **Training Information:**
  - Training Algorithms: CNN using 5 folds Cross-validation
  - Parameters: batch size, epochs, folds, random state, shuffle
  - Features: : MNIST images are grayscale images of handwritten digits, each of size 28x28 pixels. The images can not be recognized by the model if they are .PNG. The pixel values ranging from 0 to 255. 
- **Paper or Resource for More Information:** (https://ieeexplore.ieee.org/document/9451544)
- **License:** No-license

## Intended Use

- **Primary Intended Uses:** Recognition of digits inside images or texts taken from student' scholar tests in order to get the final grade for each student
- **Primary Intended Users:** Professors
- **Out-of-Scope Use Cases:** Diagnosis of dysortography; Images where the represented number is greater than 10.

## Factors

- **Relevant Factors:** Different handwriting styles, image brightness, image light or dark background, image rotation, image sharpness
- **Evaluation Factors:** Network depth, network width and cardinality

## Metrics

- **Model Performance Measures:** Accuracy
- **Decision Thresholds:** 90%

## Evaluation Data

- **Datasets:** MNIST database
- **Motivation:** The MNIST database is a large database of handwritten digits commonly used for training various image processing systems. The database is also widely used for training and testing in the field of machine learning. (https://en.wikipedia.org/wiki/MNIST_database)
- **Preprocessing:**

```pyton 
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
```  
  

## Training Data

- **Distribution Over Factors in Training Datasets:** The dataset is composed of a training set of 60,000 examples and a test set of 10,000 examples

## Quantitative Analyses

- **Unitary Results:** 
![image](https://github.com/AndreaBasile97/DigitsRecognition/assets/156330529/48b885c8-ca58-4af1-a353-bce3a4393a1b)

## Ethical Considerations

This project aims to recognize grades on students tests. Wrong predictions can led to wrong grades reporting and potentially harm the students.

## Caveats and Recommendations

The model can fail when digits are not clearly written. In order to get a good predictions we recommend to write numbers in a clear

## Model requirements checklist

- **Minimum accuracy expectations:** 90%
- **Runtime needs:** The model needs to run in a range of time of few seconds to few minutes.
- **Safety and fairness concerns in the system:** Concerning safety requirements, if there are handwritten digits that can look alike, the model needs to distinguish them to provide a precise output.
- **Security and privacy concerns in the system:** The model outputs have to be accessible only by the model users and the addressed students. The other students can't access these data.
- **Data availability:** Link to dataset card: (https://github.com/AndreaBasile97/DigitsRecognition/tree/main/data)



