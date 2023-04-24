import cell
from cell import Cell
import pygame
from constants import *
import sys
from sudoku_generator import SudokuGenerator

pygame.init()
pygame.display.set_caption('Sudoku')
screen = pygame.display.set_mode((WIDTH, 500))
board_surface = pygame.Surface((WIDTH, 500))
screen.fill((191, 239, 255))
board_surface.fill((202, 225, 255))
pygame.display.flip()
font = pygame.font.Font(None, 20)

class Board:
  CELL_SIZE = 50
  def __init__(self, width, height, screen, difficulty):
    self.width = width
    self.height = height
    self.screen = screen
    self.difficulty = difficulty
    self.user_fill = None
    self.sketches = set()


  def draw(self):
      pygame.init()
      pygame.display.set_caption('Sudoku')
      screen = pygame.display.set_mode((WIDTH, 500))
      board_surface = pygame.Surface((WIDTH, 500))
      screen.fill((191, 239, 255))
      board_surface.fill((202, 225, 255))
      pygame.display.flip()
      font = pygame.font.Font(None, 20)
      for row in range(9):
          for col in range(9):
              x = col * Board.CELL_SIZE
              y = row * Board.CELL_SIZE
              pygame.draw.rect(board_surface, (96,123,139), (x, y, Board.CELL_SIZE, Board.CELL_SIZE), 1)
      for i in range(10):
          if i % 3 == 0:
              pygame.draw.line(board_surface, (96, 123, 139), (0, i * Board.CELL_SIZE), (WIDTH, i * Board.CELL_SIZE), 4)
              pygame.draw.line(board_surface, (96, 123, 139), (i * Board.CELL_SIZE, 0), (i * Board.CELL_SIZE, WIDTH), 4)
      screen.blit(board_surface, (0, 0))

      button_width = Board.CELL_SIZE
      button_height = Board.CELL_SIZE // 2
      spacing = 10


      button_a = 50
      button_y = 500 - spacing - button_height
      button_surface = pygame.Surface((button_width, button_height))
      pygame.draw.rect(button_surface, (255,240,245), (0, 0, button_width, button_height))
      pygame.draw.rect(button_surface, (171,130,255), (0, 0, button_width, button_height), 2)
      text = font.render("Reset", True, (39,64,139))
      text_rect = text.get_rect(center=(button_width // 2, button_height // 2))
      button_surface.blit(text, text_rect)
      board_surface.blit(button_surface, (button_a, button_y))



      button_b = 200
      button_surface = pygame.Surface((button_width, button_height))
      pygame.draw.rect(button_surface, (255, 240, 245), (0, 0, button_width, button_height))
      pygame.draw.rect(button_surface, (171, 130, 255), (0, 0, button_width, button_height), 2)
      text = font.render("Restart", True, (39, 64, 139))
      text_rect = text.get_rect(center=(button_width // 2, button_height // 2))
      button_surface.blit(text, text_rect)
      board_surface.blit(button_surface, (button_b, button_y))


      button_c = 350
      button_surface = pygame.Surface((button_width, button_height))
      pygame.draw.rect(button_surface, (255, 240, 245), (0, 0, button_width, button_height))
      pygame.draw.rect(button_surface, (171, 130, 255), (0, 0, button_width, button_height), 2)
      text = font.render("Exit", True, (39, 64, 139))
      text_rect = text.get_rect(center=(button_width // 2, button_height // 2))
      button_surface.blit(text, text_rect)
      board_surface.blit(button_surface, (button_c, button_y))

      screen.blit(board_surface, (0, 0))
      pygame.display.update()

  def select(self,row, col):
    self.selected_cell = (row, col)
    cell.red_box(row, col)



  def click(self, x, y):
    cell_width = self.width // 9
    cell_height = self.height // 9
    row = y // cell_height
    col = x // cell_width

    if 0 <= col < 9 and 0 <= row < 9:
        return (row, col)
    else:
        return None


  def clear(self):
      if self.user_fill:
          self.value = None



  def sketch(self, value):
      for cell in Cell.objects:
          if cell == self.selected_cell and cell.value == 0:
              cell.sketches.add(value)






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
