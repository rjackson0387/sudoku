import pygame
from constants import *
# This shoul work

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
        if event.type == pygame.MOUSEBUTTONDOWN:
            if middle_button_rect.collidepoint(event.pos):
                start_screen()






