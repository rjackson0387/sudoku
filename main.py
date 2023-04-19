import pygame, sys
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

pygame.init()
pygame.display.set_caption("Sudoku")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

while True:
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()  # updates screen when overlayign objects on screen