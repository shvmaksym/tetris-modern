from grid import Grid
from blocks import *

import random

class Run:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [LBlock(), JBlock(), IBlock(), OBlock(), SBlock(), TBlock(), ZBlock(), XBlock(), CBlock()]
        random.shuffle(self.blocks)
        self.game_over = False
        self.current = self.get_random_block()
        self.next = self.get_random_block()
        self.score = 0
        self.speed = 500
        self.level = 1
        self.speed_changed = False

    
    def change_speed(self):
        if self.score >= 10 * self.level and self.level != 10:
            self.speed -= 40
            self.level += 1
            self.speed_changed = True


    def change_score(self, move_points, lines):
        self.score += move_points
        if lines == 1:
            self.score += 100
        elif lines == 2:
            self.score += 250
        elif lines == 3:
            self.score += 500


    def reset(self):
        self.grid.reset()
        self.game_over = False
        self.blocks = [LBlock(), JBlock(), IBlock(), OBlock(), SBlock(), TBlock(), ZBlock(), XBlock(), CBlock()]
        self.current = self.get_random_block()
        self.next = self.get_random_block()
        self.game_over = False
        self.score = 0
        self.speed = 500


    def get_random_block(self):
        if self.blocks:
            block = self.blocks.pop()
            return block
        else:
            self.blocks = [LBlock(), JBlock(), IBlock(), OBlock(), SBlock(), TBlock(), ZBlock(), XBlock(), CBlock()]
            random.shuffle(self.blocks)
            return self.get_random_block()
    

    def draw(self, screen):
        self.grid.draw(screen)
        self.current.draw(screen, 1, 1)


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
        self.current.rotate()
        if not self.game_field():
            self.current.cancel_rotation()


    def game_field(self):
        positions = self.current.get_positions()
        for tile in positions:  
            if not self.grid.block_inside(tile.row, tile.column):
                return False
        return True 


    def save_block(self):
        if not self.fits_block():
            self.game_over = True
            return
        positions = self.current.get_positions()
        for position in positions:
            self.grid.grid[position.row][position.column] = self.current.id
        self.current = self.next
        self.next = self.get_random_block()
        lines = self.grid.full_row_clear()
        self.change_score(0, lines)
        

    def fits_block(self):
        positions = self.current.get_positions()
        for position in positions:
            if not self.grid.block_empty(position.row, position.column):
                return False
        return True
    