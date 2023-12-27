class Colors:
    black = (0, 0, 0)
    cyan = (0, 255, 255)
    yellow = (255, 255, 0)	
    purple = (128, 0, 128)	
    green = (0, 255, 0)	
    red = (255, 0, 0)	
    blue = (0, 0, 255)	
    orange = (255, 127, 0)
    pink = (182,86,140)
    violet = (48,10,111)
    white = (255, 255, 255)
    screen_color = (73, 6, 72)


    @classmethod
    def get_cell_color(cls):
        return [cls.black, cls.cyan, cls.yellow, cls.purple, cls.green, cls.red, cls.blue, cls.orange, cls.pink, cls.violet]