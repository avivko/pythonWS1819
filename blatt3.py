from random import *
import numpy as np


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


def dot_vek(v1, v2):
    assert (len(v1) == len(v2)), "Vectors have different dimensions!"
    dotproduct = 0
    for i in range(len(v1)):
        dotproduct += v1[i] * v2[i]
    return dotproduct


def transpose(m):
    transposed_matrix = []
    for i in range(len(m[0])):
        row = []
        for j in range(len(m)):
            row.append(m[j][i])
        transposed_matrix.append(row)
    return transposed_matrix


def add(m1, m2):
    assert len(m1) == len(m2) and len(m1[0]) == len(m2[0]), " matrices have different dimensions"
    sum_matrix = []
    for i in range(len(m1)):
        row = []
        for j in range(len(m1[0])):
            row.append(m1[i][j] + m2[i][j])
        sum_matrix.append(row)
    return sum_matrix


def subtract(m1, m2):
    assert len(m1) == len(m2) and len(m1[0]) == len(m2[0]), " matrices have different dimensions"
    sum_matrix = []
    for i in range(len(m1)):
        row = []
        for j in range(len(m1[0])):
            row.append(m1[i][j] - m2[i][j])
        sum_matrix.append(row)
    return sum_matrix


def int_list_to_array_list(x):
    new_list = []
    for i in x:
        if isinstance(i, int):
            new_list.append([i])
    if not new_list:
        return x
    else:
        return new_list


def dot_mat(m1, m2):
    assert len(m1[0]) == len(m2), "Number of columns in the first matrix and the number of rows in the second matrix " \
                                  "do not match "
    multiplied_matrix = []
    for i in range(len(m1)):
        row = []
        for j in range(len(m2[0])):
            summe = 0
            for x in range(len(m1[0])):
                summe += m1[i][x] * m2[x][j]
            row.append(summe)
        multiplied_matrix.append(row)
    return multiplied_matrix
