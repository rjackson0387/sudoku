from sudoku_generator import SudokuGenerator

board = SudokuGenerator(0)
SudokuGenerator.print_board(board)






# board[0][1] = 1

print(board.valid_in_row(0,1))
print(board.valid_in_box(0,0,0))