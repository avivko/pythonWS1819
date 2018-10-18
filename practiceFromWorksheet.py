from typing import List


def part_one_one(n):
    for i in range(0, n):
        print(2 ** i)


def part_one_two_version_one(n):
    biggest = 0
    for i in range(0, n):
        if biggest <= n:
            biggest = 2 ** i
        else:
            biggest = biggest / 2
            return round(biggest)


def part_one_two_version_two(n):
    biggest = 1
    one_bigger = 1
    while one_bigger <= n:
        biggest = one_bigger
        one_bigger = one_bigger * 2
    return biggest


# sum numbers
def part_one_three(n):
    summe = 0
    for i in range(0, n):
        summe = summe + i
    return summe


# make table of multiplication
def part_one_four(n):
    table = []
    for i in range(1, n + 1):
        column = []
        for j in range(1, n + 1):
            column.append(i * j)
        table.append(column)
    return table


# check for prime number
def part_one_five(n):
    assert (isinstance(n, int) or (isinstance(n, float) and n.is_integer())), "Invalid input"
    int(n)
    for i in (2, n):
        if n % i == 0:
            return False
        else:
            return True


print(part_one_five(0))