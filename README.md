# Image decompression using SVD
## Introduction 
The Singular Value Decomposition (SVD) algorithm is a powerful tool for dimensionality reduction and data compression. 
SVD decomposes a matrix into three separate matrices: U, Σ, and V^T. U contains the left singular vectors, Σ is a diagonal matrix containing the singular values, and V^T represents the right singular vectors. 
The SVD algorithm allows us to approximate the original matrix by selecting a subset of singular vectors and values.

## Theory
A = U Σ V^T

- U (left singular vectors) is an orthogonal matrix whose columns are the eigenvectors of AA^T
- Σ (singular values) is a diagonal matrix containing the square roots of the eigenvalues of AA^T or A^T A
- V^T (right singular vectors) is the transpose of an orthogonal matrix whose columns are the eigenvectors of A^T A

SVD decomposes the original matrix A into three matrices that capture its structural information:

- U represents the directions of the data
- Σ represents the magnitude (singular values) of the data
- V^T represents the coordinates of the data in the new space

This decomposition enables various applications, such as dimensionality reduction, image compression, and data imputation.

## Decompression site using streamlit 
![Screen Recording 2024-08-06 161015 gif](https://github.com/user-attachments/assets/a4e92427-643f-4853-b030-c1ecd83ad520)
