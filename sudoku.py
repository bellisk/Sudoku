#Converting between text and grid representations of sudokus.

def parse(text):
	return [[int(c) for c in row] for row in text.split("\n")]

def listify(grid):
	for row in grid:
		for x in range(9):
			if row[x] == 0:
				row[x] = [1,2,3,4,5,6,7,8,9]
	return grid

def emit(grid):
	return "\n".join(["".join([str(c) for c in row]) for row in grid])

def simple_representation(grid):
	return "\n".join(["".join(["?" if type(c) == list else str(c) for c in row]) for row in grid])

#Isolating rows, columns and subgrids, and checking them for completeness and validity.

def get_row(grid, row_index):
	return grid[row_index]

def get_column(grid, column_index):
	return [row[column_index] for row in grid]

def get_subgrid(grid, subgrid_row_index, subgrid_column_index):
	subgrid = []
	for y in range(3*subgrid_row_index, 3*subgrid_row_index + 3):
		for x in range(3*subgrid_column_index, 3*subgrid_column_index + 3):
			subgrid.append(grid[y][x])
	return subgrid

def valid(shape):
	return all([type(c) == list or shape.count(c) == 1 for c in shape])

def complete(shape):
	return all([type(c) != list for c in shape])

def valid_row(grid, row_index):
	return valid(get_row(grid, row_index))

def valid_column(grid, column_index):
	return valid(get_column(grid, column_index))

def complete_row(grid, row_index):
	return complete(get_row(grid, row_index))

def complete_column(grid, column_index):
	return complete(get_column(grid, column_index))

def valid_subgrid(grid, subgrid_row_index, subgrid_column_index):
	return valid(get_subgrid(grid, subgrid_row_index, subgrid_column_index))

def complete_subgrid(grid, subgrid_row_index, subgrid_column_index):
	return complete(get_subgrid(grid, subgrid_row_index, subgrid_column_index))

def get_shapes(grid):
	shapes = []
	for y in range(9):
		shapes.append(get_row(grid, y))
	for x in range(9):
		shapes.append(get_column(grid, x))
	for y in range(3):
		for x in range(3):
			shapes.append(get_subgrid(grid, y, x))
	return shapes

#Checking full grids for validity, completeness and solvedness.

def valid_grid(grid):
	return all([valid(s) for s in get_shapes(grid)])

def complete_grid(grid):
	return all([complete(s) for s in get_shapes(grid)])

def solved_grid(grid):
	return valid_grid(grid) and complete_grid(grid)

#Start solving sudoku.

def clean_grid(grid):
	for row in grid:
		for cell_index in range(len(row)):
			cell = row[cell_index]
			if type(cell) == list and len(cell) == 1:
				row[cell_index] = cell[0]

def solve(grid):
	made_progress = True
	while made_progress and not solved_grid(grid):
		#print simple_representation(grid)
		#print "---------"
		made_progress = False
		for shape in get_shapes(grid):
			numbers = []
			for cell in shape:
				if type(cell) == int:
					numbers.append(cell)
			for n in numbers:
				for cell in shape:
					if type(cell) == list and n in cell:
						cell.remove(n)
						made_progress = True
			clean_grid(grid)
	return grid

