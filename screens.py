import pygame
from constants import *
#main menu
pygame.init()
pygame.display.set_caption('Sudoku')
screen = pygame.display.set_mode((WIDTH, HEIGHT))

Welcome = "Welcome to Sudoku"
Select = "Select Game Mode:"
font = pygame.font.Font(None, 60)


screen.fill((255, 182, 193))
text_surface = font.render(Welcome, True, (0, 0, 0))
text_rect = text_surface.get_rect()
text_rect.center = (WIDTH // 2, HEIGHT // 2 - 250)
screen.blit(text_surface, text_rect)

# select game mode
text_surface = font.render(Select, True, (0, 0, 0))
text_rect = text_surface.get_rect()
text_rect.center = (WIDTH // 2, HEIGHT // 2)
screen.blit(text_surface, text_rect)


left_button_rect = pygame.Rect(200, 500, 120, 70)
middle_button_rect = pygame.Rect(400, 500, 120, 70)
right_button_rect = pygame.Rect(600, 500, 120, 70)


font = pygame.font.Font(None, 36)
left_text = font.render('BABY', True, (0, 0, 0))
middle_text = font.render('MEDIUM', True, (0, 0, 0))
right_text = font.render('HARD', True, (0, 0, 0))


#making rectangle
pygame.draw.rect(screen, (248,248,255), (left_button_rect))
text_rect = left_text.get_rect(center=left_button_rect.center)
screen.blit(left_text, text_rect)

pygame.draw.rect(screen, (248,248,255), (middle_button_rect))
text_rect = middle_text.get_rect(center=middle_button_rect.center)
screen.blit(middle_text, text_rect)

pygame.draw.rect(screen, (248,248,255), (right_button_rect))
text_rect = right_text.get_rect(center=right_button_rect.center)
screen.blit(right_text, text_rect)
pygame.display.update()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
