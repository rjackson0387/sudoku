import pygame
from constants import *


# Pushing
class Cell:
    objects = []
    original_objects = []

    def __init__(self, value, row, col, width, height, screen):
        self.value = value
        self.ogvalue = value
        self.col = col
        self.row = row
        self.width = width
        self.height = height
        self.screen = screen
        self.selected = False
        self.cell = pygame.Rect(self.row * self.width, self.col * self.height, self.width, self.height)
        Cell.objects.append(self)
        Cell.original_objects.append(self)

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self, screen):
        chip_font = pygame.font.Font(None, 40)
        chip_1_surf = chip_font.render('1', True, NUM_COLOR)
        chip_2_surf = chip_font.render('2', True, NUM_COLOR)
        chip_3_surf = chip_font.render('3', True, NUM_COLOR)
        chip_4_surf = chip_font.render('4', True, NUM_COLOR)
        chip_5_surf = chip_font.render('5', True, NUM_COLOR)
        chip_6_surf = chip_font.render('6', True, NUM_COLOR)
        chip_7_surf = chip_font.render('7', True, NUM_COLOR)
        chip_8_surf = chip_font.render('8', True, NUM_COLOR)
        chip_9_surf = chip_font.render('9', True, NUM_COLOR)
        if self.ogvalue == 1:
            chip_1_rect = chip_1_surf.get_rect(
                center=(self.width // 2 + self.width * self.row, self.height // 2 + self.height * self.col))
            screen.blit(chip_1_surf, chip_1_rect)
        elif self.ogvalue == 2:
            chip_2_rect = chip_2_surf.get_rect(
                center=(self.width // 2 + self.width * self.row, self.height // 2 + self.height * self.col))
            screen.blit(chip_2_surf, chip_2_rect)
        elif self.ogvalue == 3:
            chip_3_rect = chip_3_surf.get_rect(
                center=(self.width // 2 + self.width * self.row, self.height // 2 + self.height * self.col))
            screen.blit(chip_3_surf, chip_3_rect)
        elif self.ogvalue == 4:
            chip_4_rect = chip_4_surf.get_rect(
                center=(self.width // 2 + self.width * self.row, self.height // 2 + self.height * self.col))
            screen.blit(chip_4_surf, chip_4_rect)
        elif self.ogvalue == 5:
            chip_5_rect = chip_5_surf.get_rect(
                center=(self.width // 2 + self.width * self.row, self.height // 2 + self.height * self.col))
            screen.blit(chip_5_surf, chip_5_rect)
        elif self.ogvalue == 6:
            chip_6_rect = chip_6_surf.get_rect(
                center=(self.width // 2 + self.width * self.row, self.height // 2 + self.height * self.col))
            screen.blit(chip_6_surf, chip_6_rect)
        elif self.ogvalue == 7:
            chip_7_rect = chip_7_surf.get_rect(
                center=(self.width // 2 + self.width * self.row, self.height // 2 + self.height * self.col))
            screen.blit(chip_7_surf, chip_7_rect)
        elif self.ogvalue == 8:
            chip_8_rect = chip_8_surf.get_rect(
                center=(self.width // 2 + self.width * self.row, self.height // 2 + self.height * self.col))
            screen.blit(chip_8_surf, chip_8_rect)
        elif self.ogvalue == 9:
            chip_9_rect = chip_9_surf.get_rect(
                center=(self.width // 2 + self.width * self.row, self.height // 2 + self.height * self.col))
            screen.blit(chip_9_surf, chip_9_rect)


saved_cell = None


def red_box(self, x, y):
    global saved_cell
    for item in Cell.objects:
        if item.cell.collidepoint((x, y)):
            pygame.draw.rect(item.screen, pygame.Color("red"), item.cell, width=1)
            if item.cell != saved_cell and saved_cell != None:
                pygame.draw.rect(item.screen, pygame.Color((96, 123, 139)), saved_cell, width=1)
            saved_cell = item.cell