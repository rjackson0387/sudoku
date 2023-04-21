import pygame, sys
from constants import *

pygame.init()
pygame.display.set_caption('Sudoku')
screen = pygame.display.set_mode((900, 900))
screen.fill(WHITE)

def draw():
    for i in range(0, 9):
        if i ==2 or i == 5 or i == 7:
            pygame.draw.line(screen, (0, 0, 0),
                             (0, i * 100),
                             (900, i * 100), BIG_LINE_WIDTH)
        else:
            pygame.draw.line(screen, (0,0,0),
                             (0, i * 100),
                             (900, i * 100))
    for j in range (0,9):
        pygame.draw.line(screen, (0,0,0), )

draw()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit

    pygame.display.update()