import numpy as np


def matrix_add(A, B):
    """
    Function for Matrix Addition
    """
    A = np.array(A)
    B = np.array(B)
    res = np.zeros(A.shape)
    for i in range(len(A)):
        for j in range(len(A)):
            res[i][j] = A[i][j] + B[i][j]
    return res


def matrix_sub(A, B):
    """
    Function for Matrix Subtraction
    """
    A = np.array(A)
    B = np.array(B)
    res = np.zeros(A.shape)
    for i in range(len(A)):
        for j in range(len(A)):
            res[i][j] = A[i][j] - B[i][j]
    return res


def matrix_multiplication(A, B):
    """
    Function For Matrix Multiplication
    """
    A = np.array(A)
    B = np.array(B)
    res = np.zeros((len(A),len(B[0])))
    for i in range(len(A)):
        for j in range(len(B)):
            for k in range(len(A[0])):
                res[i][j] += A[i][k] * B[k][j]
    return res


def transpose(A):
    """
    Function to make matrix transpose
    """
    return np.array(A).T


def inverse(A):
    """
    Function to calculation inverse matrix
    """
    A = np.array(A)
    a = A[0][0]
    b = A[0][1]
    c = A[1][0]
    d = A[1][1]
    res = []
    determina = (a * d) - (b * c)
    matrix_mod = np.array([[d, -b], [-c, a]])
    for i in range(len(matrix_mod)):
        row = []
        for j in range(len(matrix_mod[0])):
            c = determina * matrix_mod[i][j]
            row.append(c)
        res.append(row)
    return np.array(res)


def rank(A):
    """
    Function to calculation rank of matrix
    """
    A = np.array(A)
    m = len(A)
    n = len(A[0])

    rank = 0
    row = 0

    for col in range(n):
        pivot = row
        while pivot < m and abs(A[pivot][col]) < 1e-10:
            pivot += 1
        if pivot == m:
            continue
        A[row], A[pivot] = A[pivot], A[row]
        pivot_val = A[row][col]
        for j in range(col, n):
            A[row][j] /= pivot_val
        for i in range(m):
            if i != row:
                factor = A[i][col]
                for j in range(col, n):
                    A[i][j] -= factor * A[row][j]
        rank += 1
        row += 1
        if row == m:
            break
    return rank


def determinat(A):
    """
    fuction to calculation determinat 2 x 2 or 3 x 3
    """
    A = np.array(A)
    if len(A) == 2:
        a = A[0][0]
        b = A[0][1]
        c = A[1][0]
        d = A[1][1]
        return a*d - b*c
    elif len(A) == 3:
        a = A[0][0]
        b = A[0][1]
        c = A[0][2]
        d = A[1][0]
        e = A[1][1]
        f = A[1][2]
        g = A[2][0]
        h = A[2][1]
        i = A[2][2]
        return a*e*i + b*f*g + c*d*h - c*e*g - b*d*i - a*f*h
    else:
        raise ValueError("Index Error")


def gaussian_elimination(A, B):
    """
    Function to calculation gaussian elimination
    """
    A = np.array(A, dtype=float)
    b = np.array(B, dtype=float)
    n = len(b)
    for k in range(n - 1):
        if A[k, k] == 0:
            for i in range(k + 1, n):
                if A[i, k] != 0:
                    A[[k, i]] = A[[i, k]]
                    b[[k, i]] = b[[i, k]]
                    break
        for i in range(k + 1, n):
            m = A[i, k] /A[k, k]
            A[i, k+1:] -= m * A[k, k+1:]
            b[i] -= m * b[k]
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i+1:])) / A[i, i]
    return x


def LU(A):
    """
    Fuction to calculation LU decomposition
    """
    A = np.array(A)
    L = np.identity(len(A))
    U = np.copy(A)

    for k in range(len(A) - 1):
        for i in range(k + 1, len(A)):
            if U[k, k] == 0:
                raise ValueError("Pivot zeros find")
            L[i, k] = U[i, k] / U[k, k]
            for j in range(k, len(A)):
                U[i, j] -= L[i, k] * U[k, j]
    return L, U
