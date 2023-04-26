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
    pygame.display.update()



  def click(self, x, y):
    selected_cell = None

    cell_width = self.width // 9
    cell_height = self.height // 9
    row = y // cell_height
    col = x // cell_width

    if 0 <= col < 9 and 0 <= row < 9:
        return (row, col)
    else:
        return None


  def clear(self, x, y):
      sketched_value = Cell.set_sketched_value
      for cell in Cell.objects:
          if sketched_value != 0:
                  cell.set_sketched_value(None)
                  cell.draw(self.screen)
                  pygame.display.update(cell.cell)






  def sketch(self, value, x, y):
      sketch_font = pygame.font.Font(None, 20)
      row, col = self.click(x, y)
      for cell in Cell.objects:
          if cell.cell.collidepoint(x, y):
              if cell.value == 0:
                cover_sketch = pygame.Rect((50 * col+3), (50 * row + 4), 20, 20)
                pygame.draw.rect(screen, (202,225,255), cover_sketch)
                cell.set_sketched_value(value)
                sketch_surface = sketch_font.render(str(value), True, (115,115,115))
                sketch_rect = sketch_surface.get_rect(center =((50 * col) + 10, (50 * row) + 10))
                self.screen.blit(sketch_surface, sketch_rect)




  def place_number(self, cell, value, x, y, game_board):
    row, col = self.click(x,y)
    game_board[row][col] = value
    cell.set_cell_value(value)
    cover_sketch = pygame.Rect((50 * col + 3), (50*row+3), 20,20)
    pygame.draw.rect(screen, (202,225,255), cover_sketch)
    sketch_font = pygame.font.Font(None, 40)
    sketch_surface = sketch_font.render(str(value), True, (0, 0, 0))
    sketch_rect = sketch_surface.get_rect(center=cell.cell.center)
    self.screen.blit(sketch_surface, sketch_rect)

  def reset_to_original(self):
    pass
  def is_full(self, game_board):
    for item in game_board:
        if 0 in item:
            return False
    return True

  def update_board(self):
    pass
  def find_empty(self):
    pass

  def check_board(self, game_board):
      # Check rows
      for row in game_board:
          if len(set(row)) != 9:
              return False

      # Check columns
      for col in range(9):
          if len(set([game_board[row][col] for row in range(9)])) != 9:
              return False

      #Check 3x3 boxes
      for row in range(0, 9, 3):
          for col in range(0, 9, 3):
              box = [game_board[i][j] for i in range(row, row + 3) for j in range(col, col + 3)]
              if len(set(box)) != 9:
                  return False

      #If all checks pass, the game_board is valid
      return True