# Python program to inverse
# a matrix using numpy 

# import required package
import numpy as np

# Taking a 3 * 3 matrix
A = np.array(
    [[35, 53, 12],
    [12, 21, 5],
    [2, 4, 1]]
)

# Calculating the inverse of the matrix
A = np.linalg.inv(A)
print(A)
A = np.mod(A, 27)
B=np.array([
    [0, 15, 4, 20, 25],
    [23, 6, 7, 1, 1],
    [16, 16, 6, 17, 4]
])
R = A@B
print(R%27)
for sub in R:
    for x in sub:
        print(type(x))

R = np.rint(R)
R = R.astype(int)
print(R%27)
