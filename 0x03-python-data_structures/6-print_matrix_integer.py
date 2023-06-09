#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for mat in matrix:
        sp = ""
        for m in mat:
            print("{:s}{:d}".format(sp, m), end="")
            sp = " "
        print()
