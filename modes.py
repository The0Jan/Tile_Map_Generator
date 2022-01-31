from cordinates import Cordinates
from arrays import Arrays
from PIL import Image

def make_cordinates_islands(height, width, grass , sand, rock):
    """
    This method creates an instance of the class Cordinates
    and later changes changes the numbers for every surface type using this classes methods.
    After that it assumes the amount of water center points.
    Input: (heights,width,grass,sand,rock) = integers
    Returns: list_of_points = a list of numbers for each surface
    Returns: center_points = a list of cordinates in an x,y array 
    """

    cordinates = Cordinates(height, width, grass, rock, sand)
    cordinates.assume_water()
    cordinates.count_types()

    list_of_points = cordinates.list_types()
    center_points = cordinates.generate_cordinates()

    return list_of_points,center_points
    



def make_cordinates_custom(height, width, grass, sand, rock, water):
    """
    This method creates an instance of the class Cordinates
    and later changes changes the numbers for every surface type using this classes methods.
    Input: (heights, width, grass, sand, rock, water) = integers
    Returns: list_of_points = a list of numbers for each surface
    Returns: center_points = a list of cordinates in an x,y array 
    """
    
    cordinates = Cordinates(height, width, grass, rock, sand, water)
    cordinates.count_types()

    list_of_points = cordinates.list_types()
    center_points = cordinates.generate_cordinates()

    return list_of_points,center_points


def create_from_coordinates(height, width, list_of_points=[], center_points=[] ):
    """
    This method creates an instance of the class Arrays. Using this classes methods it creates 
    an 3 dimesnional array, from which an image is made.
    Input height,width = integers
    Input: list_of_points = a list of numbers for each surface
    Input: center_points = a list of cordinates in an x,y array 
    Return: image(tile map)
    """
    arrays = Arrays(height, width)
    arrays.voronoi(list_of_points, center_points)
    arrays.convert_array()
    img = arrays.show_image()
    return img