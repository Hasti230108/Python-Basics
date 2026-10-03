import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits

# Load dataset
digits = load_digits()

# Select an image
image = digits.images[0]
print("Original Image Shape:")
print(image.shape)

# SVD
U, S, VT = np.linalg.svd(image)
# Number of singular values
k = 3

# Compression
compressed_image = (
U[:, :k]
@ np.diag(S[:k])
@ VT[:k, :]
)

# Original image
plt.figure(figsize=(5, 5))
plt.imshow(image, cmap="gray")
plt.title("Original Image")
plt.axis("off")
plt.show()

# Compressed image
plt.figure(figsize=(5, 5))
plt.imshow(compressed_image, cmap="gray")
plt.title("SVD Compressed Image")
plt.axis("off")
plt.show()