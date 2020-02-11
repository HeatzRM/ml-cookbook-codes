from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# Generate feature matrix and target vector
features, target = make_blobs(
    n_samples=100,
    n_features=2,
    centers=3,
    cluster_std=0.5,
    shuffle=True,
    random_state=1,
)

# View feature matrix and target cevtor
print("Feature Matrix\n", features[:3])
print("Target Matrix\n", target[:3])

# View scatterplot
plt.scatter(features[:, 0], features[:, 1], c=target)
plt.show()
