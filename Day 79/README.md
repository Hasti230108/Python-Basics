# Day 79 — SVD Image Compression

Today I learned about **Singular Value Decomposition (SVD)** and used it for **image compression** with Python.

I used the **Scikit-learn Digits dataset**, NumPy, and Matplotlib to load an image, apply SVD, and reconstruct a compressed version of the image.

## Topics Covered

* Singular Value Decomposition (SVD)
* Matrix decomposition
* Singular values
* Image representation as a matrix
* Image compression
* NumPy `linalg.svd()`
* Scikit-learn Digits dataset
* Matplotlib image visualization
* Low-rank approximation

## 1. Loading the Dataset

I used the Digits dataset from Scikit-learn:

```python
from sklearn.datasets import load_digits

digits = load_digits()
```

The dataset contains handwritten digit images represented as numerical matrices.

## 2. Selecting an Image

```python
image = digits.images[0]
```

The selected image is represented as a matrix of pixel values.

The program displays its shape using:

```python
print(image.shape)
```

## 3. Applying SVD

```python
U, S, VT = np.linalg.svd(image)
```

SVD decomposes the image matrix into three matrices:

```text
A = U × S × VT
```

Where:

* `U` → Left singular vectors
* `S` → Singular values
* `VT` → Transpose of right singular vectors

## 4. Selecting Singular Values

```python
k = 3
```

Only the first 3 singular values are used for reconstruction.

This creates a **low-rank approximation** of the original image.

## 5. Reconstructing the Image

```python
compressed_image = (
    U[:, :k]
    @ np.diag(S[:k])
    @ VT[:k, :]
)
```

The selected components are multiplied together to reconstruct the compressed image.

## 6. Visualizing the Result

Matplotlib is used to display:

* Original image
* SVD compressed image

This allows us to visually compare the original image with its compressed version.

## Key Takeaways

> SVD decomposes a matrix into three matrices.

> Images can be represented as numerical matrices.

> Keeping fewer singular values creates a low-rank approximation.

> SVD can be used for image compression.

> A smaller `k` gives stronger compression but usually loses more detail.

## Libraries Used

```text
NumPy
Matplotlib
Scikit-learn
```