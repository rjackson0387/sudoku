from constants import *
import sudoku_generator
import random
import board
import pygame
import sys
from board import button_dict

pygame.init()





def start_screen():
    pygame.init()
    pygame.display.set_caption('Sudoku')
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    Welcome = "Welcome to Sudoku"
    Select = "Select Game Mode:"
    font = pygame.font.Font(None, 40)

    screen.fill((205, 96, 144))
    text_surface = font.render(Welcome, True, (0, 0, 0))
    text_rect = text_surface.get_rect()
    text_rect.center = (WIDTH // 2, HEIGHT // 2 - 70)
    screen.blit(text_surface, text_rect)

    # select game mode
    text_surface = font.render(Select, True, (0, 0, 0))
    text_rect = text_surface.get_rect()
    text_rect.center = (WIDTH // 2, HEIGHT // 2)
    screen.blit(text_surface, text_rect)

    left_button_rect = pygame.Rect(50, 280, 100, 40)
    middle_button_rect = pygame.Rect(180, 280, 100, 40)
    right_button_rect = pygame.Rect(300, 280, 100, 40)

    font = pygame.font.Font(None, 36)
    left_text = font.render('EASY', True, (0, 0, 0))
    middle_text = font.render('MEDIUM', True, (0, 0, 0))
    right_text = font.render('HARD', True, (0, 0, 0))

    # making rectangle
    pygame.draw.rect(screen, (248, 248, 255), (left_button_rect))
    text_rect = left_text.get_rect(center=left_button_rect.center)
    screen.blit(left_text, text_rect)

    pygame.draw.rect(screen, (248, 248, 255), (middle_button_rect))
    text_rect = middle_text.get_rect(center=middle_button_rect.center)
    screen.blit(middle_text, text_rect)

    pygame.draw.rect(screen, (248, 248, 255), (right_button_rect))
    text_rect = right_text.get_rect(center=right_button_rect.center)
    screen.blit(right_text, text_rect)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if left_button_rect.collidepoint(event.pos):
                    return 30
                elif middle_button_rect.collidepoint(event.pos):
                    return 40
                elif right_button_rect.collidepoint(event.pos):
                    return 50
def resetbutton():
    board.screen.blit(board.board_surface, (0, 0))
    button_width = board.Board.CELL_SIZE
    button_height = board.Board.CELL_SIZE // 2
    spacing = 10
    button_a = 50
    button_y = 500 - spacing - button_height
    button_surface = pygame.Surface((button_width, button_height))
    pygame.draw.rect(button_surface, (255, 240, 245), (0, 0, button_width, button_height))
    pygame.draw.rect(button_surface, (171, 130, 255), (0, 0, button_width, button_height), 2)
    text = board.font.render("Reset", True, (39, 64, 139))
    text_rect = text.get_rect(center=(button_width // 2, button_height // 2))
    button_surface.blit(text, text_rect)
    board.board_surface.blit(button_surface, (button_a, button_y))
    board.screen.blit(board.board_surface, (0, 0))
def restartbutton():
    board.screen.blit(board.board_surface, (0, 0))
    button_width = board.Board.CELL_SIZE
    button_height = board.Board.CELL_SIZE // 2
    spacing = 10
    button_b = 200
    button_y = 500 - spacing - button_height
    button_surface = pygame.Surface((button_width, button_height))
    pygame.draw.rect(button_surface, (255, 240, 245), (0, 0, button_width, button_height))
    pygame.draw.rect(button_surface, (171, 130, 255), (0, 0, button_width, button_height), 2)
    text = board.font.render("Reset", True, (39, 64, 139))
    text_rect = text.get_rect(center=(button_width // 2, button_height // 2))
    button_surface.blit(text, text_rect)
    board.board_surface.blit(button_surface, (button_b, button_y))
    board.screen.blit(board.board_surface, (0, 0))
def exitbutton(mouse_pos):
    button_rect = pygame.Rect(350, 475, 50, 25)
    if button_rect.collidepoint(mouse_pos):
        pygame.quit()
        sys.exit()


difficulty = start_screen()
game = sudoku_generator.generate_sudoku(9, difficulty)

sudoku = board.Board(WIDTH, HEIGHT, board.screen, difficulty)
sudoku.draw()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            exitbutton(mouse_pos)

    pygame.display.update()



