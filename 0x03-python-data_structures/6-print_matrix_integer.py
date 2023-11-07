#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for row in range(len(matrix)):
            for i in range(len(matrix[row])):
                if i != len(matrix[row]) - 1:
                    print("{:d}".format(matrix[row][i]), end=" ")
                else:
                    print("{:d}".format(matrix[row][i]), end="")
            print()
