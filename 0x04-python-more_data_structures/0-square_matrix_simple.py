#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
	"""
	Squares all elements in a matrix.

	Args:
		matrix: A 2D list of integers.

	Returns:
		A new 2D list with squared elements.
	"""
	return [[element ** 2 for element in row] for row in matrix]
