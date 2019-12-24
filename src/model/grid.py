from .hex import Hex as Hex

class Grid:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.hexes = {}

    def clear(self):
        self.hexes = {}

    def fill_blank(self):
        for x_coordinate in range(self.width):
            for y_coordinate in range(self.height):
                self.hexes[(x_coordinate,y_coordinate)] = Hex()

    def get_hex(self, x_coordinate, y_coordinate):
        point = (x_coordinate, y_coordinate)
        if self.hexes.has_key(point):
            return self.hexes[point]
        else:
            raise Exception("Grid doesn't have a point at {}, {}.".format(x_coordinate, y_coordinate))
