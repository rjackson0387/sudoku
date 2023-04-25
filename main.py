import pygame

import cell
from constants import *
import sudoku_generator
import random
import board
import pygame
import sys
from cell import Cell

pygame.init()


def exitbutton(coords):
    button_rect = pygame.Rect(350, 475, 50, 25)
    if button_rect.collidepoint(coords):
        pygame.quit()
        sys.exit()
def restartbutton(coords):
    button_rect = pygame.Rect(200, 475, 50, 25)
    if button_rect.collidepoint(coords):
        return True
    return False

def resetbutton(coords):
    button_rect = pygame.Rect(50, 475, 50, 25)
    if button_rect.collidepoint(coords):
        return True
    return False

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

while True: #New while loop
    difficulty = start_screen()
    restart_key = 0
    #game_board is the list with 0s, game_board_orig is the original list with no cells removed (aka the answer)
    game_board, game_board_orig = sudoku_generator.generate_sudoku(9, difficulty)
    for row, list in enumerate(game_board):
        for col, item in enumerate(list):
            Cell(item, col, row, 50, 50, board.screen)

    sudoku = board.Board(WIDTH, HEIGHT, board.screen, difficulty)
    sudoku.draw()

    for item in Cell.objects:
        item.draw(item.screen)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
                coords = event.pos
                if exitbutton(coords):
                    pygame.quit()
                    sys.exit()
                if restartbutton(coords):
                    sudoku.draw()
                    start_screen()
                    restart_key = 1
                    item = []
                    Cell.objects = []
                    break
                selected_cell = board.Board.click(sudoku, *coords)
                cell.red_box(*coords)
                if selected_cell:
                    board.Board.select(sudoku, *selected_cell)
                if resetbutton(coords):
                    sudoku = board.Board(WIDTH, HEIGHT, board.screen, difficulty)
                    sudoku.draw()

                    for item in Cell.objects:
                        item.draw(item.screen)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 or event.key == pygame.K_9 or event.key == pygame.K_2 or event.key == pygame.K_3 \
                        or event.key == pygame.K_4 or event.key == pygame.K_5 or event.key == pygame.K_6 or event.key == pygame.K_7 \
                        or event.key == pygame.K_8:
                    number_input = event.key - pygame.K_0
                    sudoku.sketch(number_input, *coords)
                    sudoku.is_full()
                elif event.key == pygame.K_BACKSPACE:
                    for cell in Cell.objects:
                        if cell.selected:
                            board.Board.clear(cell)
        pygame.display.update()
        if restart_key == 1:
            break
    pygame.display.update()
    if restart_key == 1:
        continue
