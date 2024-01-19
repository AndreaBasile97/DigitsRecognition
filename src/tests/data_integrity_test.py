from deepchecks.vision.checks import ImagePropertyOutliers
from deepchecks.vision.datasets.classification.mnist_tensorflow import load_dataset

train_data = load_dataset(train=True, object_type="VisionData")
check = ImagePropertyOutliers()
result = check.run(train_data)
print(result.value)
