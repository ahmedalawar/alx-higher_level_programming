#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        l = 1
        for i in row:
            if l == len(row):
                print("{:d}".format(i), end="")
            else:
                print("{:d}".format(i), end=" ")
            l += 1
        print("$")
