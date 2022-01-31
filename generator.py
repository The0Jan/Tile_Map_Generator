from modes import make_cordinates_islands, make_cordinates_custom, create_from_coordinates
from PIL import Image

def image_islands(height, width, grass, sand, rock):
    """ Tile map generation - default method
    This method combines earlier methods, so that only by getting the values of 
    two parameters(the width and height of the array) and the center points of some surfaces (grass,sand,rock),
    it gives a ready image.
    Input: height,width,grass,sand,rock = integer
    Output: Image (tile map)
    """
    cordinates_islands = make_cordinates_islands(height, width, grass, sand, rock)
    islands_image = create_from_coordinates(height, width, cordinates_islands[0], cordinates_islands[1])
    return islands_image

def image_custom(height, width, grass, sand, rock, water):
    """ Tile map generation - custom method
    This method combines earlier methods, so that only by getting the values of 
    two parameters(the width and height of the array) and the center points of some surfaces (grass,sand,rock,water),
    it gives a ready image.
    Input: height,width,grass,sand,rock,water = integer
    Output: Image (tile map)
    """
    cordinates_custom = make_cordinates_custom(height, width, grass, sand, rock, water)
    custom_image = create_from_coordinates(height, width, cordinates_custom[0], cordinates_custom[1])
    return custom_image

def measurments(parameter = ""):
    """
    This method asks the user a certain vaule (in form of a string), checks if the value is correct(integer).
    
    Input: parameter = string
    User_Input: str
    Return: integer
    """
    try:
        measurement = abs(int(input(parameter)))
        if measurement == 0:
            print("Parameter given can't be 0.")
            return measurments(parameter)
        else:
            return measurement
    except ValueError:
        print("Please type in an integer.")
        return measurments(parameter)

def specified_center_points(asking = ""):
    """
    This method asks the user for a str, converts into a value and checks,
    whether the  value is correct.(in this case an integer)
    Input: asking = string
    User_input: string
    Return: integer
    """
    try:
        points_amount = abs(int(input(asking)))
        return points_amount
    except ValueError:
        print("Amount given must ba an integer.")
        return specified_center_points(asking)

def simple_question(question =""):
    """
    Method used for asking the user a (no/yes) question and checking for correct answers.
    Input: question = str
    User_input: str
    Return: 0 or 1
    """
    answer = input(question)
    if answer in ('yes', 'Yes', 'YES', 'yEs', 'yeS'):
        return 1
    elif answer in ('no', 'NO', 'No', 'nO'):
        return 0
    else:
        print('Answer unrecognizable. Please answer with "yes" or "no".')
        return simple_question(question)

def zoom_map(image, width, height):
    """
    Method used for asking the user whether to zoom/enlarge the given image for him.
    Input: width, height = integers
    User_input: answer = str (yes/no)
    User_input: times = str (integer)
    Return: image
    """
    answer = input("Do you want to zoom the image?  ")

    if answer in ('yes', 'Yes', 'YES', 'yEs', 'yeS'):
        times = abs(int(input("How many times do you want to zoom it?  ")))
        newsize = (height*times, width*times)
        image = image.resize(newsize)
        image.show()
        image.load()
        zoom_map(image, width*times, height*times)
    elif answer in ('no', 'NO', 'No', 'nO'):
        return image
    else:
        print('Answer unrecognizable. Please answer with "yes" or "no".')
        return zoom_map(image, width, height)

def process_of_generating(height, width, default):
    """
    This method asks the user to give certain vaules, and later using that it creates an image, that the user can zoom.
    The user can also ,if unsatisfied, create an image(a tile map), from the beginning.
    Input: height,width = integers
    Input: default = 1 or 0
    User_input: grass,sand,rock,water = strings (to integer)
    User_input: reroll = str (to 0 or 1)
    """
    if default == 1:
        print("Default map generation process...")
        print('----------------------------------')
        grass = specified_center_points("How many 'grass' center points do you wish for? ")
        sand = specified_center_points("How many 'sand' center points do you wish for? ")
        rocks = specified_center_points("How many 'rock' center points do you wish for? ")
    
        generated_map = image_islands(height, width, grass, sand, rocks)
        generated_map.show()
        zoom_map(generated_map, width, height)
    else:
        print("Custom map generation process...")
        print('----------------------------------')
        water = specified_center_points("How many 'water' center points do you wish for? " )
        grass = specified_center_points("How many 'grass' center points do you wish for? ")
        sand = specified_center_points("How many 'sand' center points do you wish for? ")
        rocks = specified_center_points("How many 'rock' center points do you wish for? ")

        generated_map = image_custom(height, width, grass, sand, rocks, water)
        generated_map.show()
        zoom_map(generated_map, width, height)
    
    reroll = simple_question("Do you dislike the image and want to try again? -->")
        
    if reroll == 1:
        process_of_generating(height, width, default)
    else:
        return generated_map
