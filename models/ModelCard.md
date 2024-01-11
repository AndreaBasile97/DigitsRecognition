# Model Card

## Model Details

- **Person or Organization Developing Model:** Basile Andrea, Di Lago Maria Grazia, Pizzillo Valentina, Saltarelli Silvia
- **Model Date:** 11/01/2024
- **Model Version:** 1.0
- **Model Type:** CNN
- **Training Information:**
  - Training Algorithms: [Algorithms Used]
  - Parameters: [Parameter Details]
  - Fairness Constraints: [Fairness Constraints]
  - Features: [Features Used]
- **Paper or Resource for More Information:** (https://ieeexplore.ieee.org/document/9451544)
- **Citation Details:** [Citation Details]
- **License:** [License Details]
- **Where to Send Questions or Comments:** [Contact Information]

## Intended Use

- **Primary Intended Uses:** Recognition of ciphers inside images or texts 
- **Primary Intended Users:** Everyone
- **Out-of-Scope Use Cases:** Diagnosis of dysortography

## Factors

- **Relevant Factors:** [List of Relevant Factors]
- **Evaluation Factors:** network depth, network width and cardinality

## Metrics

- **Model Performance Measures:** [List of Performance Measures]
- **Decision Thresholds:** [List of Decision Thresholds]
- **Variation Approaches:** [List of Variation Approaches]

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

- **Distribution Over Factors in Training Datasets:** [Details on Distribution]

## Quantitative Analyses

- **Unitary Results:** [Results of Unitary Analyses]
- **Intersectional Results:** [Results of Intersectional Analyses]

## Ethical Considerations

[Discuss any ethical considerations related to the model]

## Caveats and Recommendations

[Provide any caveats and recommendations related to the model]
