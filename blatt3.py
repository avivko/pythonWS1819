from random import *


def rand(m, n):
    matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(randrange(0, 2))
        matrix.append(row)
    return matrix


def identity(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    return matrix


def dot(v1,v2):
    assert (len(v1) == len(v2)), "Vectors have different dimensions!"
    dotproduct = 0
    for i in range(len(v1)):
        dotproduct += v1[i] * v2[i]
    return dotproduct


