from sudoku_generator import SudokuGenerator

board = SudokuGenerator(0)
SudokuGenerator.print_board(board)
# board[0][1] = 1

print(board.is_valid(0,0,0))