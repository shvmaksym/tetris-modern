import pygame
from colors import Colors

class Grid:
    def __init__(self):
        self.rows = 30
        self.columns = 20
        self.cell_size = 50
        self.colors = Colors.get_cell_color()
        self.grid = [[0 for j in range(self.columns)] for i in range(self.rows)]

    
    def draw(self, screen):
        for row in range(self.rows):
            for column in range(self.columns):
                cell = self.grid[row][column]
                cell_rect = pygame.Rect(column*self.cell_size + 1, row*self.cell_size + 1, self.cell_size - 1, self.cell_size - 1)
                pygame.draw.rect(screen, self.colors[cell], cell_rect)