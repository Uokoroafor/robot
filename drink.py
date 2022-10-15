import random


class Drink:
    def __init__(self, filename='drink_names.txt', auto=True):
        """ This initialises a drinks class """
        if auto:
            names = []
            textfile = open(filename)

            for line in textfile:
                name = line.strip()  # This strips off the '/n' at the end of each line
                names.append(name)
            my_name = names[random.randint(0, len(names) - 1)]
        else:
            my_name = str(input('Please enter the name of the drink you want the robot to seek out'))
        self.name = my_name
