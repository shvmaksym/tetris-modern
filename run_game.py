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
        