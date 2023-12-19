from colors import Colors

class Block:
    def __init__(self):
        self.id = id
        self.cells = {}
        self.cell_size = 50
        self.rotation = 0
        self.colors = Colors.get_cell_color()
