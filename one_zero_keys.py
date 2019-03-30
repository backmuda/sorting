import numpy as np
import string


def main_algorithm(A):

    A_length = len(A[0])  # indices start with zero in python.
    i = 0
    for j in range(A_length):
        if A[0][i] == 1:
            key = A[0][i]
            key_alpha = A[1][i]
            A[0][i:A_length - 1] = A[0][i + 1: A_length]
            A[1][i:A_length - 1] = A[1][i + 1: A_length]
            A[0][A_length - 1] = key
            A[1][A_length - 1] = key_alpha
        else:
            i += 1

    return A


def bare_algorithm(a):

    i = 0
    length_a = len(a)
    for j in range(length_a):
        if a[i] == 1:
            key = a[i]
            a[i:length_a - 1] = a[i + 1: length_a]
            a[length_a - 1] = key
        else:
            i += 1

    return a


if __name__ == '__main__':

    array_length = 26
    random_ones_zeros = list(np.random.choice([0, 1], array_length))  # Uniformly random one's and zeros.
    match_alphabet = string.ascii_uppercase[0:array_length]
    A = [random_ones_zeros, list(match_alphabet)]
    print(A[0])
    print(A[1])
    print()
    A = main_algorithm(A)
    print(A[0])
    print(A[1])
    print()

    a = list(np.random.choice([0, 1], array_length))
    b = bare_algorithm(a)
    print(b)

