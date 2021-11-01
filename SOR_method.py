#author : Zahra Dehghanitafti(96222037)
import numpy
import numpy as np

#the goal of this code is to solve the Ax = b system with iterative method(SOR method)
n = int(input("Enter the number of rows and columns:"))

entries_A = list(map(int, input("Please enter entries of matrix A").split()))
entries_b = list(map(int, input("Please enter entries of vector b").split()))
entries_x1 = list(map(int, input("Please enter entries of vector x1").split()))

A = np.array(entries_A).reshape(n, n) #input matrix A (square matrix)
b = np.array(entries_b).reshape(n, 1)
x1 = np.array(entries_x1).reshape(n, 1) #any arbitrary choice of the initial approximation

#relaxation parameter
w = float(input("Please enter relaxation parameter"))

L = numpy.zeros((n,n)) #lower triangular matrix
D = numpy.zeros((n,n)) #diagonal matrix
U = numpy.zeros((n,n)) #upper triangular matrix

for i in range(n): #move along rows
    for j in range(n): #move along columns
        if i == j:
            D[i][j] = A[i][j] #create diagonal matrix from A
        if i < j:
            U[i][j] = A[i][j] #create upper triangular matrix from A
        if i > j:
            L[i][j] = A[i][j] #create lower triangular matrix from A

B_sor = np.dot(numpy.linalg.inv(D + np.dot(w,L)),np.dot((1 - w),D) - np.dot(w,U))

b_sor = np.dot(np.dot(w,numpy.linalg.inv(D + np.dot(w,L))), b)

x = np.linalg.solve(A, b) #answer of system (Ax=b)

for i in range(20):# Repeat the algorithm for 20 times
    print("norm of (x - x1) = " ,np.linalg.norm(x-x1)) #The difference between the original answer and the answer in each iteration
    x1 = np.dot(B_sor, x1) + b_sor #the answer in each iteration
    print("x1 = ", x1)
    print("_____________________________")
