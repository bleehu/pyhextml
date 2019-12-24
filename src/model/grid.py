from . import Hex as Hex

class grid:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.hexes = {}