#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        leng = 1
        for i in row:
            if leng == len(row):
                print("{:d}".format(i), end="")
            else:
                print("{:d}".format(i), end=" ")
            leng += 1
        print("")

