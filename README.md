Digits Recognition
==============================

## Project Overview

This project aims to develop an AI-enabled system focused on digit recognition from images using a Convolutional Neural Network (CNN). A CNN is a type of artificial neural network renowned for its efficacy in image recognition and processing, owing to its capacity to discern patterns in images[^1^].

CNNs necessitate extensive labeled datasets for training, often in the order of millions of data points. Furthermore, to ensure swift and practical results, training CNNs demands high-performance processors such as Graphics Processing Units (GPUs) or Neural Processing Units (NPUs)[^1^].

## Convolutional Neural Network (CNN) Architecture

A CNN comprises multiple layers, each dedicated to learning distinct features within an image. Filters are systematically applied to training images at varying resolutions, with the output of each convolutional layer serving as the input for the subsequent layer. The filters typically start by identifying basic features like brightness or edges and progressively evolve to encompass more intricate features that uniquely characterize the object being recognized[^2^].

For further insights, refer to the glossary provided by ARM on Convolutional Neural Networks [^1^] and MathWorks' comprehensive exploration of CNNs[^2^].

[^1^]: [ARM - Convolutional Neural Network](https://www.arm.com/glossary/convolutional-neural-network#:~:text=A%20convolutional%20neural%20network%20(CNN)%20is%20a%20type%20of%20artificial,to%20recognize%20patterns%20in%20images)

[^2^]: [MathWorks - Convolutional Neural Network](https://it.mathworks.com/discovery/convolutional-neural-network.html)


Project Organization
------------



    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
