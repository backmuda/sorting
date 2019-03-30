import numpy as np
import string


def binary_sort(A):

    i = 0
    j = len(A[0]) - 1
    while i < j:
        if A[0][i] == 1:
            while A[0][j] == 1 and i < j:
                j -= 1
            A[0][i], A[0][j] = A[0][j], A[0][i]
            A[1][i], A[1][j] = A[1][j], A[1][i]
            j -= 1
        i += 1

    return A


def binary_sort_bare(A):

    i = 0
    j = len(A) - 1
    while i < j:
        if A[i] == 1:
            while A[j] == 1 and i < j:
                j -= 1
            A[i], A[j] = A[j], A[i]
            j -= 1
        i += 1

    return A


if __name__ == '__main__':

    array_length = 26
    random_ones_zeros = list(np.random.choice([0, 1], array_length))  # Uniformly random one's and zeros.
    match_alphabet = string.ascii_uppercase[0:array_length]
    A = [random_ones_zeros, list(match_alphabet)]
    print(A[0])
    print(A[1])
    print()
    A = binary_sort(A)
    print(A[0])
    print(A[1])
    print()

    a = list(np.random.choice([0, 1], 40))
    b = binary_sort_bare(a)
    print(b)
