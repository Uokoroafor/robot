from drink import drink
from robot_init import RobotFactory


def move_all_to_drink(grid, robot_count=3):
    """This is the root function that takes robot details and navigates it to the Ribena
    Args:
        grid_size (int): The size of the grid
        robot_count (int): The number of robots taking part"""

    SkyNet = RobotFactory(grid=grid)
    robots = SkyNet.create_robots(grid=grid, count=robot_count)
    for robot in robots:
        robot.print_greeting()

    for robot in robots:
        target_drink = drink()
        robot.print_search()
        robot.print_location()
        navigate_to_drink(robot, grid=grid, drink=target_drink)


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


def navigate_to_drink(robot, grid, drink):
    """ This navigates to the corner cell of the grid with the drink"""
    drink_name = drink.name
    grid_size = grid.size
    end_pos = grid._get_end_position()

    end_row, end_col = end_pos[0], end_pos[1]
    target = False
    while ((robot.position[1] != grid_size - 1) or (robot.position[0] != grid_size - 1)) or not target:
        wall = False
        while not wall:
            robot.move_forward(grid_size=grid_size)
            wall = grid._wall_test(robot.position, robot.direction)
            cardinal = get_direction_string(robot.direction)
            print(f'My current location is ({robot.position}), facing {cardinal}')

            if (robot.position[0] == end_pos[0]) and (robot.position[1] == end_pos[1]):
                target = True
                break
        if (robot.position[0] == end_pos[0]) and (robot.position[1] == end_pos[1]):
            target = True
            break

        print('I have a wall in front of me!')
        robot.turn_90_degrees()

    print('I am now drinking ' + drink_name + ' and happy!')
    print('***' * 10)