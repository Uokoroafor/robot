from NavigationManager import move_all_to_drink
from grid import Grid

# Now to run the experiment
if __name__ == '__main__':
    my_grid = Grid(5)
    print(my_grid)
    move_all_to_drink(robot_count=3, grid=my_grid, delay=False)

