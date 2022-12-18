from NavigationManager import *
from grid import Grid

# Now to run the experiment
if __name__ == '__main__':
    my_grid = Grid(5)
    move_all_to_drink(robot_count=3, grid=my_grid, delay=True)

