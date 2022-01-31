import numpy as np
import random
from PIL import Image

class Arrays:
    """
    Class that creates 3 arrays and operates on them.
    Input argumnets width,height: integers
    """
    def __init__(self, height, width):
       
        self.color_array = np.zeros([width, height], int)
        self.value_array = np.ones([width, height], float)* 1e308
        self.array_3 = np.zeros((width, height, 3), np.int8)
       
        self.width = width
        self.height = height

        self.green = [0, 250, 0]
        self.grey = [150, 150, 150]
        self.yellow = [200, 200, 0]
        self.blue = [0, 0, 250]

    def show_color(self):
        print(self.color_array)
    
    def show_value(self):
        return self.array_3

    def throw_value(self):
        print(self.array_3)
    
    def voronoi(self, list_isle, points):
        """
        Method, that uses a list of cordinates(points) and a list of the amount of surface types.
        Operates on two of the classes arrays and creates an extra array.
        It counts the hypotenuse for every point in a x,y array and puts it into the 'nearest' array,
        then it checks whether the number in the  x,y cordinates is smaller then the one in the value_array.
        For all thoose x,y cordinates where it actually is smaller ,
        it overlaps the color_array value with a number from list_isle, and the value_array with the number from the 'nearest' array.
        
        Input: list_isle = list of number
        Input: points = list of cordinates in an x,y array

        Returns: A changed color_array and value_array
        """

        def hypotenuse(X,Y):
            return (X-x)**2 + (Y-y)**2


        for i,(x,y) in enumerate(points):
            color = list_isle[i]
            nearest = np.fromfunction(hypotenuse,(self.width,self.height))
            self.color_array = np.where(nearest < self.value_array,color,self.color_array)
            self.value_array = np.where(nearest <
                                    self.value_array,nearest,self.value_array)

    
    def convert_array(self):
        """
        This method for every number positioned in the color_array assigns a specific list in a 3-dimensional array.
        The lists portray certain colors.
        This method is used to create a 3 dimensional array of colors.
        Returns: three dimensional array of colors
        """
        for cordinate_x in range(0, self.width ):
            for cordinate_y in range(0, self.height):
                x = cordinate_x
                y = cordinate_y
                if self.color_array[x, y] == 0: #woda
                    self.array_3[x, y] = self.blue
                elif self.color_array[x, y] == 1:  #trawa
                    self.array_3[x, y] = self.green
                elif self.color_array[x, y] == 2:  #żwir
                    self.array_3[x, y] = self.grey
                elif self.color_array[x, y] == 3:  #piasek
                    self.array_3[x, y] = self.yellow
        return self.array_3
     
    def show_image(self):
        """
        Creates an image from the three dimensional array.
        Returns: Image
        """
        img = Image.fromarray(self.array_3, 'RGB')
        return img 



