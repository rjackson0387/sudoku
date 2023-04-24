import pygame
from constants import *

#main menu
pygame.init()
pygame.display.set_caption('Sudoku')
screen = pygame.display.set_mode((WIDTH, HEIGHT))

Game_Won = "Game Won!"
font = pygame.font.Font(None, 40)

screen.fill((205,96,144))
text_surface = font.render(Game_Won, True, (0, 0, 0))
text_rect = text_surface.get_rect()
text_rect.center = (WIDTH // 2, HEIGHT // 2 - 70)
screen.blit(text_surface, text_rect)


middle_button_rect = pygame.Rect(180, 200, 100, 40)
middle_text = font.render('EXIT', True, (0, 0, 0))


#middle button

pygame.draw.rect(screen, (248,248,255), (middle_button_rect))
text_rect = middle_text.get_rect(center=middle_button_rect.center)
screen.blit(middle_text, text_rect)
pygame.display.update()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False






