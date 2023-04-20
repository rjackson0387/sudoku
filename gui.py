import pygame
from constants import *


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False




