from cell import Cell
import pygame
from constants import *
import sys

pygame.init()
pygame.display.set_caption('Sudoku')
screen = pygame.display.set_mode((WIDTH, HEIGHT))   # (453, 453) makes it around the actual parts of the board
board_surface = pygame.Surface((WIDTH, HEIGHT))
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


  def draw(self):
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


      button_x = 50
      button_y = HEIGHT - spacing - button_height
      button_surface = pygame.Surface((button_width, button_height))
      pygame.draw.rect(button_surface, (255,240,245), (0, 0, button_width, button_height))
      pygame.draw.rect(button_surface, (171,130,255), (0, 0, button_width, button_height), 2)
      text = font.render("Reset", True, (39,64,139))
      text_rect = text.get_rect(center=(button_width // 2, button_height // 2))
      button_surface.blit(text, text_rect)
      board_surface.blit(button_surface, (button_x, button_y))



      button_x = 200
      button_surface = pygame.Surface((button_width, button_height))
      pygame.draw.rect(button_surface, (255, 240, 245), (0, 0, button_width, button_height))
      pygame.draw.rect(button_surface, (171, 130, 255), (0, 0, button_width, button_height), 2)
      text = font.render("Restart", True, (39, 64, 139))
      text_rect = text.get_rect(center=(button_width // 2, button_height // 2))
      button_surface.blit(text, text_rect)
      board_surface.blit(button_surface, (button_x, button_y))


      button_x = 350
      button_surface = pygame.Surface((button_width, button_height))
      pygame.draw.rect(button_surface, (255, 240, 245), (0, 0, button_width, button_height))
      pygame.draw.rect(button_surface, (171, 130, 255), (0, 0, button_width, button_height), 2)
      text = font.render("Exit", True, (39, 64, 139))
      text_rect = text.get_rect(center=(button_width // 2, button_height // 2))
      button_surface.blit(text, text_rect)
      board_surface.blit(button_surface, (button_x, button_y))


      screen.blit(board_surface, (0, 0))
      pygame.display.update()






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
