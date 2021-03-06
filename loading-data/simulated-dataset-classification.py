# Load library
from sklearn.datasets import make_classification

# Generate features matrix and target vector
features, target = make_classification(
    n_samples=100,
    n_features=3,
    n_informative=3,
    n_redundant=0,
    n_classes=2,
    weights=[0.25, 0.75],
    random_state=1,
)

# View feature matrix and target cevtor
print("Feature Matrix\n", features[:3])
print("Target Matrix\n", target[:3])
