from drink import Drink
from robot_init import RobotFactory
import random
from grid import BattleGrid


def move_all_to_drink(grid, robot_count=3, delay=False):
    """This is the root function that takes robot details and navigates it to the Ribena
    Args:
        grid (object): The size of the grid
        robot_count (int): The number of robots taking part
        delay (bool): Whether to print the board after each step"""

    print('Welcome to the Robot Navigation Manager')

    skynet = RobotFactory(grid=grid)
    robots = skynet.create_robots(grid=grid, count=robot_count)
    for robot in robots:
        robot.print_greeting()

    for robot in robots:
        target_drink = Drink()
        robot.print_search()
        robot.print_location()
        navigate_to_drink(robot, grid=grid, drink=target_drink, delay=delay)


def get_direction_string(txt):
    """ Converts direction into full text """
    if txt == 'n':
        return 'North'
    elif txt == 's':
        return 'South'
    elif txt == 'e':
        return 'East'
    elif txt == 'w':
        return 'West'


def navigate_to_drink(robot, grid, drink, delay=False):
    """ This navigates to the corner cell of the grid with the drink"""
    drink_name = drink.name
    grid_size = grid.size
    end_pos = grid.get_end_position()
    print('Initial setup of grid')
    grid.print_grid(r_pos=robot.position, d_pos=end_pos, delay=False)
    target = False  # True if Robot has arrived at target

    while (robot.position[1] != grid_size - 1) or (robot.position[0] != grid_size - 1) or target == False:
        wall = False
        while not wall:
            robot.move_forward(grid_size=grid_size)
            wall = grid.wall_test(robot.position, robot.direction)
            cardinal = get_direction_string(robot.direction)
            print(f'My current location is ({robot.position}), facing {cardinal}')
            if delay:
                grid.print_grid(r_pos=robot.position, d_pos=end_pos, delay=delay)

            if (robot.position[0] == end_pos[0]) and (robot.position[1] == end_pos[1]):
                target = True
                break
        # if (robot.position[0] == end_pos[0]) and (robot.position[1] == end_pos[1]):
        if target:
            break

        print('I have a wall in front of me!')
        robot.turn_90_degrees()

    print('I am now drinking ' + drink_name + ' and happy!')
    print('***' * 10)


def progress(robot, battle_grid):
    """ This moves the robot forward"""
    grid_size = battle_grid.size

    wall = battle_grid.wall_test(robot.position, robot.direction)

    if wall:
        print('I have a wall in front of me!')
        robot.turn_90_degrees()

    robot.move_forward(grid_size=grid_size)
    robot.print_greeting()
    robot.print_location()


def battle(robots):
    # At each go, one Robot is randomly selected to go first

    while robots[0].alive and robots[1].alive:
        random.shuffle(robots)
        fight(robots)


def fight(robots):
    winner = None
    print(f'{robots[0].name} goes first.')

    robots[0].attack(robots[1])

    if not robots[1].check_alive:
        winner = robots[0]

    else:
        robots[1].attack(robots[0])

    if not robots[0].check_alive:
        winner = robots[0]

    if winner is not None:
        print(f'Winner is {winner.name}!')


def start_grid(battle_grid, delay=False):
    # grid_size = battle_grid.size
    print('Printing Empty Grid')
    battle_grid.print_grid()
    skynet = RobotFactory(battle_grid)
    robots = skynet.create_battle_robots(battle_grid)
    while not robots[0].is_enemy_close(robots[1]):
        for robot in robots:
            progress(robot, battle_grid)
            battle_grid.print_grid(sign='*', r1_pos=robots[0].position, r2_pos=robots[1].position, delay=delay)
            if robots[0].is_enemy_close(robots[1]):
                break
    battle(robots)


if __name__ == '__main__':
    my_grid = BattleGrid(5)
    pass
