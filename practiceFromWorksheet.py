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
    assert ((isinstance(n, int) or (isinstance(n, float) and n.is_integer())) and n > 0), "Invalid input"
    int(n)
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            return is_prime
    if n == 1:
        is_prime = False
    else:
        is_prime = True
    return is_prime


# check for primes under n
def part_one_six(n):
    for i in range(1, n + 1):
        if part_one_five(i):
            print(i)


# makes a table with * at desired spots. n is size of table
def part_one_seven(n):
    table = []
    for j in range(1, n + 1):
        columns = []
        for i in range(1, n + 1):
            if j % i == 0:
                columns.append("*")
            else:
                columns.append("")
            table.append(columns)
        print(columns)
    return table


# addition function
def part_two_one(a, b):
    return a + b


# sqrt
def part_two_two(n):
    return n ** 2


# returns the hypotenuse for a,b right angle triangle
def part_two_three(a, b):
    return ((a ** 2) + (b ** 2)) ** 0.5


# returns sum of 1/n series
def part_two_four(n):
    harm_num = 1
    for i in range(2, n + 1):
        harm_num = harm_num + 1 / i
    return harm_num


# return list of harmonic numbers for a list l
def part_two_five(l):
    list_of_harm = []
    for x in l:
        list_of_harm.append(part_two_four(x))
    return list_of_harm


print(part_two_five([1, 2, 3]))
