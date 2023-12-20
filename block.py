from colors import Colors
from position import Position
import pygame

class Block:
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cell_size = 50
        self.offset_row = 0
        self.offset_column = 0
        self.rotation = 0
        self.colors = Colors.get_cell_color()

    def move(self, rows, columns):
        self.offset_row += rows
        self.offset_column += columns
    
    def get_positions(self):
        tiles = self.cells[self.rotation]
        tiles_move = []
        for position in tiles:
            position = Position(position.row + self.offset_row, position.column + self.offset_column)
            tiles_move.append(position)
        return tiles_move

    def draw(self, screen):
        tiles = self.get_positions()
        for tile in tiles:
            tile_rect = pygame.Rect(tile.column * self.cell_size + 1, tile.row * self.cell_size + 1, self.cell_size - 1, self.cell_size - 1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)