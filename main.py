import sudoku_generator
from sudoku_generator import SudokuGenerator
import random
board = SudokuGenerator(9, 0)
SudokuGenerator.print_board(board)
print()
# board[0][1] = 1

print(board.is_valid(0,3,1))


board.fill_values()
SudokuGenerator.print_board(board)

print(board.valid_in_box(0,3,1))
print(board.valid_in_col(3,1))
print(board.valid_in_row(0,1))
print(board.is_valid(0,3,1))
#board.remove_cells()
print()

'''board.remove_cells()
SudokuGenerator.print_board(board)
print()'''

board = sudoku_generator.generate_sudoku(9, 30)

