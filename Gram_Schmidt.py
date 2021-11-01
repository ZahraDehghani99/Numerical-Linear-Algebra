#author : Zahra Dehghanitafti(96222037)
import math
import numpy
import numpy as np

#input matrix A (square matrix)
n = int(input("Enter the number of rows and columns:"))

entries = list(map(int, input("Please enter entries of matrix A").split()))
A = np.array(entries).reshape(n, n)

#orthogonal matrix Q
Q = numpy.zeros((n,n))

#upper triangular matrix R
R = numpy.zeros((n,n))

#vector n_dimentional y
y = [0]*n
square_of_length_of_y = 0

for j in range(0,n): # move along columns(j = 0 means that we are in 0th column)
    for i in range(0,j): # We move along rows with columns of elements above the original diameter.(Element row number above the main diameter with column number j = from 0 to j-1)
        for k1 in range(0,n):
            R[i][j] += Q[k1][i]*A[k1][j] # at this level we obtain the elements above the original diameter, because R is upper triangular matrix.
            # To obtain R we must multiply A and transpose of Q(inverse of Q).
    for l in range(0,n):
        tafrigh = 0
        for k2 in range(0,j):
            tafrigh += Q[l][k2]*R[k2][j]
        y[l] = A[l][j] - tafrigh

    for k3 in range(0,n):
        square_of_length_of_y += y[k3]**2 # calculates square of length of vector y

    R[j][j] = math.sqrt(square_of_length_of_y)  # Elements on the original diameter of matrix R
    #R[j][j] == length of y
    for i in range(0,n):
        Q[i][j] = y[i]/R[j][j]

print(R)
print(Q)
print(np.dot(Q,R))
