from grid import Grid
from blocks import *
import random

class Run:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [LBlock(), JBlock(), IBlock(), OBlock(), SBlock(), TBlock(), ZBlock(), XBlock(), CBlock()]
        self.current = self.get_random_block()
        self.next = self.get_random_block()
    
    def get_random_block(self):
        block = random.choice(self.blocks)
        return block
    
    def draw(self, screen):
        self.grid.draw(screen)
        self.current.draw(screen)

    def move_left(self):
        self.current.move(0, -1)
        if self.game_field() == False:
            self.current.move(0, 1)
    
    def move_right(self):
        self.current.move(0, 1)
        if self.game_field() == False:
            self.current.move(0, -1)

    def move_down(self):
        self.current.move(1, 0)
        if self.game_field() == False:
            self.current.move(-1, 0)
            self.save_block()

    def change_position(self):
        positions = self.current.get_positions()
        for tile in positions:
            if tile.column < 0 or tile.column >= self.grid.columns:
                return
            if tile.row < 0 or tile.row >= self.grid.rows:
                return
        self.current.rotate()

    def game_field(self):
        positions = self.current.get_positions()
        for position in positions:
            if self.grid.block_inside(position.row, position.column) == False:
                return False
        return True

    def save_block(self):
        positions = self.current.get_positions()
        for position in positions:
            self.grid.grid[position.row][position.column] = self.current.id
        self.current = self.next
        self.next = self.get_random_block()
            
    