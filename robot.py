class Robot:
    def __init__(self, identifier, name, position, direction):
        self.id = identifier
        self.name = name
        self.position = position
        self.direction = direction

    def move_forward(self, grid_size):
        print('Moving one step forward.')
        if self.direction == 'n':
            new_row = self.position[0] - 1
            new_row = max(0, new_row)
            self.position = (new_row, self.position[1])
        elif self.direction == 's':
            new_row = self.position[0] + 1
            new_row = min(grid_size - 1, new_row)
            self.position = (new_row, self.position[1])
        elif self.direction == 'e':
            new_col = self.position[1] + 1
            new_col = min(grid_size - 1, new_col)
            self.position = (self.position[0], new_col)
        elif self.direction == 'w':
            new_col = self.position[1] - 1
            new_col = max(0, new_col)
            self.position = (self.position[0], new_col)

    def turn_90_degrees(self):
        """ Changes direction 90 degrees"""
        print('Turning 90 degrees clockwise.')
        if self.direction == 'n':
            self.direction = 'e'
        elif self.direction == 's':
            self.direction = 'w'
        elif self.direction == 'e':
            self.direction = 's'
        elif self.direction == 'w':
            self.direction = 'n'
        self.print_location()

    def get_direction_string(self):
        """ Converts direction into full text """
        if self.direction == 'n':
            return 'North'
        elif self.direction == 's':
            return 'South'
        elif self.direction == 'e':
            return 'East'
        elif self.direction == 'w':
            return 'West'

    def print_greeting(self):
        """ Prints my robot's name and id"""
        print(f'Hello my name is {self.name}. My ID is {self.id}.')

    def __repr__(self):
        return f"Robot(name: {self.name}, id: {self.id}, position: ({self.position}))"

    def print_location(self):
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

        dir_string = get_direction_string(self.direction)
        print(f'My current location is ({self.position}), facing {dir_string}.')

    def print_search(self):
        print(f'{self.name} is looking for its drink.')


if __name__ == '__main__':
    # Create a Random Robot and print
    jerry = Robot(name='Jerry', identifier='001', position='5,5', direction='e')
    print(jerry)

