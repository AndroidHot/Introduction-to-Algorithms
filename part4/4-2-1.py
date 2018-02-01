# Strassen 算法
# 适用于 A B 矩阵都属于 n * n 矩阵，并且 n 为 2 的幂

import numpy as np
import time

def isPowerOfTwo(n):
    if n <= 0:
        return False
    return True if n & (n-1) == 0 else False

# square matrix multiply recursive
def smmr(matrixA, matrixB):
    n = matrixA.shape[0]    
    if matrixA.shape[0] != matrixA.shape[1] or matrixA.shape != matrixB.shape or not isPowerOfTwo(n):
        print("smmr: matrixA.shape[0] != matrixA.shape[1] or matrixA.shape != matrixB.shape  or not isPowerOfTwo(n)")
        return
    matrixC = np.zeros((n, n))
    if n == 1:
        matrixC[0][0] = matrixA[0][0] * matrixB[0][0]
    else:
        half_n = int(n / 2)
        matrixC[:half_n, :half_n] = smmr(matrixA[:half_n, :half_n], matrixB[:half_n, :half_n]) + smmr(matrixA[:half_n, half_n:], matrixB[half_n:, :half_n])
        matrixC[:half_n, half_n:] = smmr(matrixA[:half_n, :half_n], matrixB[:half_n, half_n:]) + smmr(matrixA[:half_n, half_n:], matrixB[half_n:, half_n:])
        matrixC[half_n:, :half_n] = smmr(matrixA[half_n:, :half_n], matrixB[:half_n, :half_n]) + smmr(matrixA[half_n:, half_n:], matrixB[half_n:, :half_n])
        matrixC[half_n:, half_n:] = smmr(matrixA[half_n:, :half_n], matrixB[:half_n, half_n:]) + smmr(matrixA[half_n:, half_n:], matrixB[half_n:, half_n:])
    return matrixC


def strassen(matrixA, matrixB):
    n = matrixA.shape[0]
    matrixC = np.zeros((n, n))
    if matrixA.shape[0] != matrixA.shape[1] or matrixA.shape != matrixB.shape or not isPowerOfTwo(n):
        print("strassen: matrixA.shape[0] != matrixA.shape[1] or matrixA.shape != matrixB.shape  or not isPowerOfTwo(n)")
        return
    # step 1
    half_n = int(n / 2)
    matrixA11 = matrixA[:half_n, :half_n]
    matrixA12 = matrixA[:half_n, half_n:]
    matrixA21 = matrixA[half_n:, :half_n]
    matrixA22 = matrixA[half_n:, half_n:]
    matrixB11 = matrixB[:half_n, :half_n]
    matrixB12 = matrixB[:half_n, half_n:]
    matrixB21 = matrixB[half_n:, :half_n]
    matrixB22 = matrixB[half_n:, half_n:]

    # step 2
    S1 = matrixB12 - matrixB22
    S2 = matrixA11 + matrixA12
    S3 = matrixA21 + matrixA22
    S4 = matrixB21 - matrixB11
    S5 = matrixA11 + matrixA22
    S6 = matrixB11 + matrixB22
    S7 = matrixA12 - matrixA22
    S8 = matrixB21 + matrixB22
    S9 = matrixA11 - matrixA21
    SX = matrixB11 + matrixB12

    # step 3
    P1 = smmr(matrixA11, S1)
    P2 = smmr(S2, matrixB22)
    P3 = smmr(S3, matrixB11)
    P4 = smmr(matrixA22, S4)
    P5 = smmr(S5, S6)
    P6 = smmr(S7, S8)
    P7 = smmr(S9, SX)

    # step 4
    matrixC[:half_n, :half_n] = P5 + P4 - P2 + P6
    matrixC[:half_n, half_n:] = P1 + P2
    matrixC[half_n:, :half_n] = P3 + P4
    matrixC[half_n:, half_n:] = P5 + P1 - P3 - P7

    return matrixC

testMatrixA = np.random.random((128,128))
testMatrixB = np.random.random((128,128))

time1 = time.time()
smmr(testMatrixA, testMatrixB)
time2 = time.time()
print('smmr using time: ', (time2 - time1))
strassen(testMatrixA, testMatrixB)
time3 = time.time()
print('strassen using time: ', (time3 - time2))
