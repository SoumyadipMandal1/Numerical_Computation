def rowEchelon(matrix):
	'''
	This function returns the row Echelon form of the matrix in the most optimal way.
	'''

	matrix = matrix.copy()

	if (rows := len(matrix)) == 0:
		raise ValueError("Empty Matrix")

	columns = len(matrix[0])

	# Checking if all rows have the same length
	for i in matrix[1:]: # Starting with second row because we are comparing it with the length of second row
		if len(i) != columns:
			raise ValueError("All rows of a matrix is of the same length")

	# Keeps track of rows and columns
	row, column = 0, 0

	# This loops converts the matrix into row echelon form
	while row < rows and column < columns:

		# If pivot is equal to zero
		if matrix[row][column] == 0:

			# Checking for a non-zero number below a pivot
			for i in range(row + 1, rows):
				if matrix[i][column]:

					# Swapping the two rows
					matrix[row][j], matrix[i][j] = matrix[i][j], matrix[row][j]
					break

			# If there is no non-zero number below the pivot
			else:
				# Search in the next column
				column += 1
				continue

		#If pivot is not equal to zero
		else:
			for i in range(row + 1, rows):
				# If scaling factor is zero, then there will be no changes in the column
				if matrix[i][column] == 0:
					continue

				scalingFactor = matrix[i][column] / matrix[row][column]
				matrix[i][column] = 0
				for j in range(column + 1, columns):
					matrix[i][j] -= matrix[row][j] * scalingFactor

			row += 1
			column += 1