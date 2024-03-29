import random
from leapingrobot import LeapingRobot
from robot import Robot
from battlerobot import BattleRobot


class RobotFactory:

    def __init__(self, grid, filename='name_files/robot_names.txt'):
        """ This initialises the Robot generation and creates all the necessary
        
        """
        self.grid_size = grid.size
        self.filename = filename

    def _get_name(self):
        names = []
        textfile = open(self.filename)
        for line in textfile:
            name = line.strip()  # This strips off the '/n' at the end of each line
            names.append(name)
        my_name = names[random.randint(0, len(names) - 1)]
        return my_name

    @staticmethod
    def _get_id():

        return str(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')) + str(random.randint(1, 1000))

    def _get_position(self):
        """ Initialises a random position for the robot in the square grid

        Returns:
            a 2 item tuple (row,column)"""

        row = random.randint(0, self.grid_size - 1)
        col = random.randint(0, self.grid_size - 1)
        return row, col

    @staticmethod
    def _get_direction():
        """ Initialises a random cardinal direction for the robot to start with

            Returns:
                a randomly selected compass direction from {'n','s','e','w'}"""

        compass = ['n', 's', 'e', 'w']
        direction = random.randint(0, 3)
        return compass[direction]

    def create_robots(self, grid, count=3, mode='rand'):
        """ This creates said robots.

        If mode == rand(om) (default) - it will flip a coin and
        create either a leaping or regular robot at random each time

        head for leaper, tails for regular

        if mode == 'leap' then it's fairly self-explanatory
        """
        robots = []
        for a in range(count):
            name = self._get_name()
            identifier = self._get_id()
            position = grid.get_position()
            direction = self._get_direction()

            if mode == 'rand':
                coin = random.choice(['h', 't'])
                if coin == 'h':
                    robots.append(LeapingRobot(identifier, name, position, direction))
                else:
                    robots.append(Robot(identifier, name, position, direction))
            elif mode == 'leap':
                robots.append(LeapingRobot(identifier, name, position, direction))

            else:
                robots.append(Robot(identifier, name, position, direction))
        return robots

    def create_battle_robots(self, battle_grid):
        """ This creates battle robots."""
        robots = []
        for _ in range(2):
            name = self._get_name()
            identifier = self._get_id()
            position = battle_grid.get_position()
            direction = self._get_direction()
            robots.append(BattleRobot(identifier, name, position, direction))

        return robots
