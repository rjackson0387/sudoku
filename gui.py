import pygame
from constants import *

pygame.init()
pygame.display.set_caption('Sudoku')
screen = pygame.display.set_mode((WIDTH, HEIGHT))


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

