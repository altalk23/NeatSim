class Tile:
    def __init__(self, color, rect):
        self.color = color
        self.rect = rect
        self.dirty = 1

    def __str__(self):
        return f'''
        Color: {self.color}
        Rect: {self.rect}
        Dirty: {self.dirty}
        '''
