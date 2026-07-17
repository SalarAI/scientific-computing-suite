import numpy as np

def DotProduct(A, B):
    """
    Function to calculation DotProduct
    """
    A = np.array(A)
    B = np.array(B)
    res = 0
    for i in range(len(A)):
        res += A[i] * B[i]
    return np.array(res)


def CrossProduct(A, B):
    """
    Function to calculation CrossProduct
    """
    A = np.array(A)
    B = np.array(B)
    a1, b1 = A[0], B[0]
    a2, b2 = A[1], B[1]
    a3, b3 = A[2], B[2]
    xi = a2*b3 - a3*b2
    yj = a3*b1 - a1*b3
    zk = a1*b2 - a2*b1
    return np.array([xi, yj, zk])


def Magnitude(x, y, z = None):
    """
    Function to calculation Magnitude from vector
    """
    if z == None:
        return np.sqrt(x**2 + y**2)
    elif z != None:
        return np.sqrt(x**2 + y**2 + z**2)


def Projection(A, B, type="Scalar"):
    """
    Function to calculation Projection from A and B
    """
    A = np.asarray(A, dtype=float)
    B = np.asarray(B, dtype=float)
    if type.lower() == "scalar":
        num = DotProduct(A, B)
        denum = np.linalg.norm(np.array(A))
        return num / denum
    elif type.lower() == "vector":
        num = DotProduct(A, B)
        denum = DotProduct(A, A)
        return (num / denum) * A
    else:
        raise KeyError("Error")


def AngleBetweenVectors(A, B):
    """
    Function To calculation Angle Between Vectors A and B
    """
    A = np.array(A)
    B = np.array(B)
    num = DotProduct(A, B)
    denum = np.linalg.norm(A) * np.linalg.norm(B)
    return np.arccos(num / denum)


def Normalization(A):
    """
    Function to find Normalization of Vector
    """
    A = np.array(A)
    return A / np.linalg.norm(A)
