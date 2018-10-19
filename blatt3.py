from random import *


def create_random_binary_matrix(m, n):
    matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(randrange(0, 2))
        matrix.append(row)
    return matrix



