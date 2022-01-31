import random
class Cordinates:
    """
    This class takes the height and width of the planned array.
    Surface types(grass, rocks, sand, water) are changable throigh methods.
    Input arguments width, height: integers
    """
    def __init__(self, height, width, grass = 0, rocks = 0, sand = 0, water = 0):

        self.width = width
        self.height = height

        self.cordinates = []

        self.grass = grass
        self.rocks = rocks
        self.sand = sand
        self.water = water
        self.types = 0

    def set_grass(self, new_grass):
        self.grass = new_grass

    def set_rocks(self, new_rocks):
        self.rocks = new_rocks

    def set_sand(self, new_sand):
        self.sand = new_sand

    def set_water(self, new_water):
        self.water = new_water

    def assume_water(self):
        """
        Assumes the amount of 'water' type center points, based on the sum of the other types.
        Used for default mode.
        """
        area = self.rocks + self.grass + self.sand
        water = area*4
        usable_points = self.width* self.height - area
        if usable_points <  water:
            self.water = usable_points
        else:
            self.water = water

    def count_types(self):
        self.types = self.water + self.sand + self.grass + self.rocks

    def list_types(self):
        """
        For every surface type it appends the amount of that typpe as a number to the list.
        (0 for water, 1 for grass, 2 for rocks, 3 for sand)
        Returns: List of numbers
        """
        types_list = []
        for _ in range(0, self.water):
            types_list.append(0)
        for _ in range(0, self.grass):
            types_list.append(1)
        for _ in range(0, self.rocks):
            types_list.append(2)
        for _ in range(0, self.sand):
            types_list.append(3)
        return types_list

    def generate_cordinates(self):
        """
        Creates n cordinates in a x,y array,adds them to a list and makes none of them to overlap.
        n = the nummber of all center points in the array (self.all_isle)
        Returns: List of cordinates
        """
        cordinates_list = []
        width = self.width
        height = self.height

        def find_random(width, height):
                x = random.randint(0,width)
                y = random.randint(0,height)
                if (x,y) in cordinates_list:
                    find_random(width, height)
                else:
                    cordinates_list.append((x,y))

        for _ in range(0, self.types):
            find_random(width, height)
        
        return cordinates_list