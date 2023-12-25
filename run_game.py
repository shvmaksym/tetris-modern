from grid import Grid
from blocks import *
import random

class Run:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [LBlock(), JBlock(), IBlock(), OBlock(), SBlock(), TBlock(), ZBlock(), XBlock(), CBlock()]
        random.shuffle(self.blocks)
        self.current = self.get_random_block()
        self.next = self.get_random_block()

    def get_random_block(self):
        if self.blocks:
            block = self.blocks.pop()
            return block
        else:
            random.shuffle(self.blocks)
            self.blocks = [LBlock(), JBlock(), IBlock(), OBlock(), SBlock(), TBlock(), ZBlock(), XBlock(), CBlock()]
            return self.get_random_block()
    
    def draw(self, screen):
        self.grid.draw(screen)
        self.current.draw(screen)

    def move_left(self):
        self.current.move(0, -1)
        if not self.game_field() or not self.fits_block():
            self.current.move(0, 1)
    
    def move_right(self):
        self.current.move(0, 1)
        if not self.game_field() or not self.fits_block():
            self.current.move(0, -1)

    def move_down(self):
        self.current.move(1, 0)
        if not self.game_field() or not self.fits_block():
            self.current.move(-1, 0)
            self.save_block()

    def change_position(self):
        positions = self.current.get_positions()
        for tile in positions:
            if 0 < tile.column >= self.grid.columns and 0 < tile.row >= self.grid.rows:
                return
            if not self.grid.block_empty(tile.row, tile.column):
                return
        self.current.rotate()

    def game_field(self):
        positions = self.current.get_positions()
        for tile in positions:  
            if not self.grid.block_inside(tile.row, tile.column):
                return False
        return True 

    def save_block(self):
        positions = self.current.get_positions()
        for position in positions:
            self.grid.grid[position.row][position.column] = self.current.id
        self.current = self.next
        self.next = self.get_random_block()
        self.grid.full_row_clear()
        
    def fits_block(self):
        positions = self.current.get_positions()
        for position in positions:
            if not self.grid.block_empty(position.row, position.column):
                return False
        return True
    