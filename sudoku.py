def parse(text):
	return [[int(c) for c in row] for row in text.split("\n")]

def emit(grid):
	return "\n".join(["".join([str(c) for c in row]) for row in grid])

def valid_row(grid, row_index):
	for c in grid[row_index]:
		if c != 0:
			if grid[row_index].count(c) > 1:
				return False
	return True

def valid_column(grid, column_index):
	column = []
	for x in range (9):
		column.append(grid[x][column_index])
	for c in column:
		if c != 0:
			if column.count(c) > 1:
				return False
	return True

def complete_row(grid, row_index):
	if len(grid[row_index]) != 9:
		return False
	if 0 in grid[row_index]:
		return False
	return True

def complete_column(grid, column_index):
	column = []
	for x in range (9):
		column.append(grid[x][column_index])
	if len(column) != 9:
		return False
	if 0 in column:
		return False
	return True

def valid_subgrid(grid, subgrid_row_index, subgrid_column_index):
	subgrid = []
	for y in range(3*subgrid_row_index, 3*subgrid_row_index + 3):
		for x in range(3*subgrid_column_index, 3*subgrid_column_index + 3):
			subgrid.append(grid[y][x])
	for c in subgrid:
		if c != 0:
			if subgrid.count(c) > 1:
				return False
	return True

def complete_subgrid(grid, subgrid_row_index, subgrid_column_index):
	subgrid = []
	for y in range(3*subgrid_row_index, 3*subgrid_row_index + 3):
		for x in range(3*subgrid_column_index, 3*subgrid_column_index + 3):
			subgrid.append(grid[y][x])
	if len(subgrid) != 9:
		return False
	if 0 in subgrid:
		return False
	return True

def valid_grid(grid):
	for y in range(9):
		if not valid_row(grid, y):
			return False
	for x in range(9):
		if not valid_column(grid, x):
			return False
	for y in range(3):
		for x in range(3):
			if not valid_subgrid(grid, y, x):
				return False
	return True

def complete_grid(grid):
	for y in range(9):
		if not complete_row(grid, y):
			return False
	for x in range(9):
		if not complete_column(grid, x):
			return False
	for y in range(3):
		for x in range(3):
			if not complete_subgrid(grid, y, x):
				return False
	return True

def solved_grid(grid):
	return valid_grid(grid) and complete_grid(grid)
