import random
from grid import Grid, BattleGrid

def print_test():
    """Initialise a grid of random size and print an empty grid"""

    test_size = random.randint(3, 5)
    test_grid = Grid(test_size)
    print(f'initialising a grid of size {test_size}. \n Please confirm visual')
    test_grid.print_grid(r_pos=(0, test_size - 1), d_pos=(test_size - 1, 0), delay=False)


def print_battle_test():
    """Initialise a grid of random size and print an empty grid"""

    test_size = random.randint(3, 10)
    battle_grid = BattleGrid(test_size)
    print(f'initialising a battle grid of size {test_size}. \n Please confirm visual')
    battle_grid.print_grid(r1_pos=(0, test_size - 1), r2_pos=(test_size - 1, 0), delay=False)


if __name__ == '__main__':
    print('Testing Grid Class')
    print_test()
    print_battle_test()