from sudoku_generator import SudokuGenerator

board = SudokuGenerator(5)
SudokuGenerator.print_board(board)
# board[0][1] = 1

print(board.is_valid(0,0,0))


board.fill_values()
SudokuGenerator.print_board(board)
print()

board.remove_cells()
SudokuGenerator.print_board(board)