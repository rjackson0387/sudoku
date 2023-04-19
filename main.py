from sudoku_generator import SudokuGenerator

board = SudokuGenerator(0)
SudokuGenerator.print_board(board)
# board[0][1] = 1

print(board.is_valid(0,0,0))
board.fill_values()
SudokuGenerator.print_board(board)
print(board.valid_in_box(0,0,0))
SudokuGenerator.print_board(board)