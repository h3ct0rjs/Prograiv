# coding: utf-8
#Sudoku Modified version from Angel Augusto
#hfjimenez@utp.edu.co

from util  import Observable
from wrapt import synchronized
import math

class Cell(Observable):

	def __init__(self, row, col):
		super(Cell, self).__init__()
		self.values = [i+1 for i in range(9)]
		self.is_solved = False
		self.row = row
		self.col = col

	def __iter__(self):
		for val in self.values:
			yield val

	def set_value(self, value):
		self.values = [value]
		self.is_solved = True
		self.notify_observers(value)

	def get_value(self):
		return self.values[0] if self.is_solved else 0

	def add_observer(self, cells):
		N = len(cells)
		for i in range(N):
			for j in range(N):
				if i == self.row and j == self.col: continue
				is_sline = (i == self.row) or (j == self.col)
				is_sbox  = (i//3 == self.row//3) and (j//3 == self.col//3)
				if is_sline or is_sbox:
					#if self.row == self.col == 5:
					#	print(self.row, self.col, i, j)
					super(Cell, self).add_observer(cells[i][j])

	@synchronized
	def update(self, value):
		if self.is_solved or value == 0: return
		#if self.row == 5 and self.col == 5:
		#	print(value, self.values)
		if value in self.values: self.values.remove(value)
		if not self.is_solved and len(self.values) == 1:
			self.set_value(self.values[0])

'''
Representa el tablero del Sudoku
'''
class Board(object):

	def __init__(self, N = 9):
		self.cells = [[Cell(i,j) for j in range(N)] for i in range(N)]

		# Adiciona observadores
		for i in range(N):
			for j in range(N):
				self.cells[i][j].add_observer(self.cells)

	def __str__(self):
		N = len(self)

		str = '+---------+---------+---------+\n'
		for i in range(N):
			str += '|'
			for j in range(N):
				value = self.cells[i][j].get_value()
				str += ' {} '.format(value if value != 0 else '.')
				if (j + 1) % 3 == 0:
					str += '|'
			str += '\n'
			if (i + 1) % 3 == 0:
				str += '+---------+---------+---------+\n'
		str += '\n' + self.candidates()

		return str

	def __len__(self):
		return len(self.cells)

	#How is the input puzzle list or string.
	def setup(self, puzzle):
		if isinstance(puzzle, list):
			self._setup_from_list(puzzle)
		elif isinstance(puzzle, str):
			self._setup_from_str(puzzle)

	def _setup_from_list(self, puzzle):
		N = len(self)
		assert len(puzzle) == N
		for i in range(N):
			for j in range(N):
				if puzzle[i][j] == 0: continue
				self.cells[i][j].setValue(puzzle[i][j])

	def _setup_from_str(self, puzzle):
		N = len(self)
		#assert math.sqrt(len(puzzle)) == N
		for i in range(N):
			for j in range(N):
				c = puzzle[i*N+j]
				if c == '.': continue
				self.cells[i][j].set_value(int(c))

	def set_value(self, row, col, value):
		self.cells[row][col].set_value(value)

	def candidates(self):
		N = len(self)
		str = ''
		for i in range(N):
			for j in range(N):
				str += 'cells[{}][{}] : '.format(i, j)
				for k in self.cells[i][j]:
					str += '{} '.format(k)
				str += '\n'
		return str

fd = open('sudoku.txt')
fd.readline()
p = fd.readline()
b = Board()
b.setup(p)
print(b)
