import sudoku
import unittest

class Tests(unittest.TestCase):

	def setUp(self):
		self.sudokuText = """407900630
030800009
000563000
504700020
029030460
070002801
000354000
700009080
065008304"""
		self.sudokuGrid = [[4,0,7,9,0,0,6,3,0],[0,3,0,8,0,0,0,0,9],[0,0,0,5,6,3,0,0,0],[5,0,4,7,0,0,0,2,0],[0,2,9,0,3,0,4,6,0],[0,7,0,0,0,2,8,0,1],[0,0,0,3,5,4,0,0,0],[7,0,0,0,0,9,0,8,0],[0,6,5,0,0,8,3,0,4]]
		self.sudokuGridSolved = [[4,5,7,9,2,1,6,3,8],[6,3,2,8,4,7,5,1,9],[9,8,1,5,6,3,7,4,2],[5,1,4,7,8,6,9,2,3],[8,2,9,1,3,5,4,6,7],[3,7,6,4,9,2,8,5,1],[2,9,8,3,5,4,1,7,6],[7,4,3,6,1,9,2,8,5],[1,6,5,2,7,8,3,9,4]]
		self.sudokuGridListified = [[4, [1, 2, 3, 4, 5, 6, 7, 8, 9], 7, 9, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 6, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], 3, [1, 2, 3, 4, 5, 6, 7, 8, 9], 8, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 9], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 5, 6, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [5, [1, 2, 3, 4, 5, 6, 7, 8, 9], 4, 7, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 2, [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 9, [1, 2, 3, 4, 5, 6, 7, 8, 9], 3, [1, 2, 3, 4, 5, 6, 7, 8, 9], 4, 6, [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], 7, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 8, [1, 2, 3, 4, 5, 6, 7, 8, 9], 1], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 5, 4, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [7, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 9, [1, 2, 3, 4, 5, 6, 7, 8, 9], 8, [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], 6, 5, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 8, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9], 4]]

	def test_parse(self):
		self.assertEqual(sudoku.parse(self.sudokuText), self.sudokuGrid)

	def test_listify(self):		
		self.assertTrue(sudoku.listify(self.sudokuGrid) == self.sudokuGridListified)

	def test_emit(self):
		self.assertEqual(sudoku.emit(self.sudokuGrid), self.sudokuText)

	def test_valid_row(self):
		self.assertTrue(sudoku.valid_row(sudoku.listify(self.sudokuGrid), 3))
		self.sudokuGridListified[0][0] = 3
		self.assertFalse(sudoku.valid_row(self.sudokuGridListified, 0))

	def test_valid_column(self):
		self.assertTrue(sudoku.valid_column(sudoku.listify(self.sudokuGrid), 3))
		self.sudokuGridListified[0][0] = 5
		self.assertFalse(sudoku.valid_column(self.sudokuGridListified, 0))

	def test_complete_row(self):
		self.assertFalse(sudoku.complete_row(self.sudokuGridListified, 3))
		self.sudokuGridListified[0] = [9, 2, 3, 4, 5, 6, 7, 8, 1]
		self.assertTrue(sudoku.complete_row(self.sudokuGridListified, 0))

	def test_complete_column(self):
		self.assertFalse(sudoku.complete_column(self.sudokuGridListified, 3))
		for x in range(9):
			self.sudokuGridListified[x][0] = 9 - x
		self.assertTrue(sudoku.complete_column(self.sudokuGridListified, 0))

	def test_valid_subgrid(self):
		self.assertTrue(sudoku.valid_subgrid(sudoku.listify(self.sudokuGrid), 1, 2))
		self.sudokuGridListified[4][7] = 4
		self.assertFalse(sudoku.valid_subgrid(self.sudokuGridListified, 1, 2))

	def test_complete_subgrid(self):
		self.assertFalse(sudoku.complete_subgrid(self.sudokuGridListified, 0, 1))
		self.sudokuGridListified[0] = [4,0,7,9,1,2,6,3,0]
		self.sudokuGridListified[1] = [0,3,0,8,4,7,0,0,9]
		self.sudokuGridListified[2] = [0,0,0,5,6,3,0,0,0]
		self.assertTrue(sudoku.complete_subgrid(self.sudokuGridListified, 0, 1))

	def test_valid_grid(self):
		self.assertTrue(sudoku.valid_grid(sudoku.listify(self.sudokuGrid)))
		self.sudokuGrid[0][0] = 5
		self.assertFalse(sudoku.valid_grid(sudoku.listify(self.sudokuGrid)))
		self.sudokuGrid[8][8] = 5
		self.assertFalse(sudoku.valid_grid(sudoku.listify(self.sudokuGrid)))
		self.sudokuGrid[0][4] = 8
		self.assertFalse(sudoku.valid_grid(sudoku.listify(self.sudokuGrid)))

	def test_complete_grid(self):
		self.assertFalse(sudoku.complete_grid(self.sudokuGridListified))
		self.assertTrue(sudoku.complete_grid(self.sudokuGridSolved))

	def test_solve(self):
		#print sudoku.simple_representation(self.sudokuGridListified)
		#print "\n"
		#print sudoku.simple_representation(sudoku.solve(self.sudokuGridListified))
		self.assertTrue(sudoku.solve(self.sudokuGridListified) == self.sudokuGridSolved)

if __name__ == '__main__':
	unittest.main()
