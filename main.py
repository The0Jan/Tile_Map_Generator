from generator import image_islands, image_custom, measurments, specified_center_points, simple_question, process_of_generating
from PIL import Image

def main(word=''):
    """
    This method asks the user for the size(width, length).
    It gives the user the posibility of creating a randolmy genarated image using the default or custom mode,
    enlarging it, saving it under a name, and reapiting the process.
    Input: word = string
    User_input: width,height = string ( to integers)
    User_input: default, save, last_question = string ( to 0 or 1)
    User_input: name = string

    """

    print(word)
    width = measurments("How wide to you want the map to be? -->")
    height = measurments("How long do you want the map to be? -->")

    default = simple_question("Do you want a default generation?  ")
    generated_map = process_of_generating(height, width, default)
    save = simple_question("Do you want to save the image? -->")

    if save == 1:
        name = input("Save as:")
        ending = name.find('.')
        if ending != -1:
            generated_map.save(name)
        else:
            corrected_name = name + '.png'
            generated_map.save(corrected_name)
    
    last_question = simple_question("Do you want to create another image? -->")

    if last_question == 1:
        main("Welcome,again.")

if __name__ == "__main__":
    """
    Method used for calling out all other methods an this program.
    Can be started by running the python file "tile_map.py" in the Terminal
    """
    main("Welcome")