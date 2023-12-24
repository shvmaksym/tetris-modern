import pygame
from colors import Colors

class Grid:
    def __init__(self):
        self.rows = 20
        self.columns = 10
        self.cell_size = 30
        self.colors = Colors.get_cell_color()
        self.grid = [[0 for _ in range(self.columns)] for _ in range(self.rows)]
    
    def draw(self, screen):
        for row in range(self.rows):
            for column in range(self.columns):
                cell = self.grid[row][column]
                cell_rect = pygame.Rect(column*self.cell_size + 1, row*self.cell_size + 1, self.cell_size - 1, self.cell_size - 1)
                pygame.draw.rect(screen, self.colors[cell], cell_rect)
    
    def block_inside(self, row, column):
        if 0 <= row < self.rows and 0 <= column < self.columns:
            return True
        return False
    
    def block_empty(self, row, column):
        if self.block_inside(row, column):
            if self.grid[row][column] == 0:
                return True
        return False
    