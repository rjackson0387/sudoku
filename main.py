import sudoku_generator
from sudoku_generator import SudokuGenerator
import random
'''board = SudokuGenerator(5)
SudokuGenerator.print_board(board)
# board[0][1] = 1

print(board.is_valid(0,0,0))


board.fill_values()
SudokuGenerator.print_board(board)

board.remove_cells()
print()

board.remove_cells()
SudokuGenerator.print_board(board)
'''
board = sudoku_generator.generate_sudoku(9.30)
print(board)
