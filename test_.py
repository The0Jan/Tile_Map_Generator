import pytest
import PIL
from cordinates import Cordinates
from arrays import Arrays

def test_list_types():
    cordinates = Cordinates(20,20,10,5,3,1)
    sample_list = cordinates.list_types()
    
    assert len(sample_list) == 19

def test_generate_cordinates():
    cordinates = Cordinates(100, 100, 12, 5, 3, 20)
    cordinates.count_types()
    cordinates.list_types()
    sample_cordinate_list = cordinates.generate_cordinates()

    assert len(sample_cordinate_list) == 40

def test_list_types_if_nothing():
    cordinates = Cordinates(20,20, 0, 0, 0, 0)
    sample_list = cordinates.list_types()
    
    assert len(sample_list) == 0

def test_generate_cordinates_if_nothnig():
    cordinates = Cordinates(100, 100, 0, 0, 0, 0)
    cordinates.count_types()
    cordinates.list_types()
    sample_cordinate_list = cordinates.generate_cordinates()

    assert len(sample_cordinate_list) == 0

def test_array_height():
    array = Arrays(15,30)
    array.voronoi([0,0,1,3], [(0,0), (15,15), (30,30), (10,27)])
    example = array.convert_array()
    assert len(example) == 30

def test_array_size():
    array = Arrays(30,40)
    array.voronoi([0,2,1,3], [(0,7), (19,15), (30,30), (10,27)])
    example = array .convert_array()
    width = 0
    for row in example:
        for _ in row:
            width += 1
    assert width == 1200
    
def test_array_image():
    array = Arrays(100,80)
    array.voronoi([0,1,3,2], [(1,1),(25,25), (69,37), (98,7)])
    array.convert_array()
    example_image = array.show_image()

    width,height = example_image.size
    assert width == 100
    assert height == 80
