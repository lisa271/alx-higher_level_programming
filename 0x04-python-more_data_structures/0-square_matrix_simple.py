#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
<<<<<<< HEAD
    new_matrix = [[x ** 2 for x in row] for row in matrix]
    return new_matrix
=======
    new_matrix = matrix.copy()

    for i in range(len(matrix)):
        new_matrix[i] = list(map(lambda x: x**2, matrix[i]))
        return (new_matrix)
>>>>>>> 53a094cce6055353bee8e4eb5a9ca6f69a439394
