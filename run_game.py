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


    def change_position(self):
        self.current.rotate()

    def game_field(self):
        tiles = self.current.get_positions()
        for tile in tiles:
            if not self.grid.block_inside(tile.row, tile.column):
                return False
        return True

    