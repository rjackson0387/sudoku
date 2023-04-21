import constants
import sudoku_generator
from sudoku_generator import SudokuGenerator
import random
import board
import pygame
import sys

#board = SudokuGenerator(9,30)

#SudokuGenerator.print_board(board)
# board[0][1] = 1
sod = board.Board(constants.WIDTH, constants.HEIGHT, board.screen, 30)
sod.draw()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

#board.fill_values()
#SudokuGenerator.print_board(board)
#board.remove_cells()


