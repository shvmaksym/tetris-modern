from colors import Colors
from position import Position
import pygame

class Block:
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.offset_row = 0
        self.offset_column = 0
        self.rotation = 0
        self.colors = Colors.get_cell_color()

    def move(self, rows, columns):
        self.offset_row += rows
        self.offset_column += columns
    
    def get_positions(self):
        tiles = self.cells[self.rotation]
        return map(lambda position: Position(position.row + self.offset_row, position.column + self.offset_column), tiles)
    
    def rotate(self):
        self.rotation += 1
        if self.rotation == len(self.cells):
            self.rotation = 0

    def draw(self, screen, offset_x, offset_y):
        tiles = self.get_positions()
        for tile in tiles:
            tile_rect = pygame.Rect(offset_x + tile.column * self.cell_size, offset_y + tile.row * self.cell_size, self.cell_size - 1, self.cell_size - 1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)

    def cancel_rotation(self):
        self.rotation -= 1
        if self.rotation == 0:
            self.rotation = len(self.cells) - 1
