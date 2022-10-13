import math
import random
from drink import drink
from grid import grid
from robot import Robot
from robot_init import RobotFactory
from NavigationManager import *


# Now to run the experiment
if __name__=='__main__':
    my_grid=grid(10)
    move_all_to_drink(robot_count=5, grid=my_grid)
