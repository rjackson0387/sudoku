from cell import Cell
import pygame
from constants import *

pygame.init()
pygame.display.set_caption('Sudoku')
screen = pygame.display.set_mode((WIDTH, HEIGHT))
board_surface = pygame.Surface((WIDTH, HEIGHT))
screen.fill((191, 239, 255))
board_surface.fill((202, 225, 255))
pygame.display.flip()


class Board:
  def __init__(self, width, height, screen, difficulty):
    self.width = width
    self.height = height
    self.screen = screen
    self.difficulty = difficulty

  def draw(self):
    for row in range(9):
        for col in range(9):
            x = col * CELL_SIZE
            y = row * CELL_SIZE
            pygame.draw.rect(board_surface, (96,123,139), (x, y, CELL_SIZE, CELL_SIZE), 1)
    for i in range(10):
        if i % 3 == 0:
            pygame.draw.line(board_surface, (96, 123, 139), (0, i* CELL_SIZE), (WIDTH, i * CELL_SIZE), 4)
            pygame.draw.line(board_surface, (96, 123, 139), (i * CELL_SIZE, 0), (i * CELL_SIZE, WIDTH), 4)
    screen.blit(board_surface, (0, 0))
    pygame.display.flip()


  def select(self,row, col):
    pass 
  def click(self, x, y):
    pass
  def sketch(self, value):
    pass
  def place_number(self, value):
    pass
  def reset_to_original(self):
    pass
  def is_full(self):
    pass
  def update_board(self):
    pass
  def find_empty(self):
    pass
  def check_board(self):
    pass
