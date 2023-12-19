import pygame

class Grid:
    def __init__(self):
        self.rows = 20
        self.columns = 10
        self.cell_size = 30
        self.colors = self.get_cell_color()
        self.grid = [[0 for j in range(self.columns)] for i in range(self.rows)]

    def get_cell_color(self):
        cyan = (0, 255, 255)
        yellow = (255, 255, 0)	
        purple = (128, 0, 128)	
        green = (0, 255, 0)	
        red = (255, 0, 0)
        blue = (0, 0, 255)
        orange = (255, 127, 0)
        grey = (127, 127, 127)	

        return [cyan, yellow, purple, green, red, blue, orange, grey]
    
    def draw(self, screen):
        for row in range(self.rows):
            for column in range(self.columns):
                cell = self.grid[row][column]
                cell_rect = pygame.Rect(column*self.cell_size + 1, row*self.cell_size + 1, self.cell_size - 1, self.cell_size - 1)
                pygame.draw.rect(screen, self.colors[-1], cell_rect)