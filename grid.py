import random


class Grid:
    def __init__(self, size=10):
        """ This initialises the grid class """
        self.size = size

    def get_end_position(self):
        """ Initialises a random end position for the robot in the square grid

        Returns:
            a 2 tuple (row,column)"""

        row = random.choice([0, self.size - 1])
        col = random.choice([0, self.size - 1])
        return row, col

    def get_position(self):
        """ Initialises a random position for the robot in the square grid
        Returns:
            a 2 item list (row,column)"""

        row = random.randint(0, self.size - 1)
        col = random.randint(0, self.size - 1)
        return row, col

    def wall_test(self, position, direction):
        """ Checks whether the robot has hit the wall or not. Will return a boolean
        Args:
            position (tuple): (row,column) that is being checked
            direction (str): The current direction
        Returns:
            True/False if the robot is/isn't at the wall"""

        row = position[0]
        col = position[1]
        grid_size = self.size
        if direction == 'n' and row <= 0:
            return True
        elif direction == 's' and row >= grid_size - 1:
            return True
        elif direction == 'e' and col >= grid_size - 1:
            return True
        elif direction == 'w' and col <= 0:
            return True
        else:
            return False

    def print_grid(self, sign='*', r_pos=None, d_pos=None, delay=False):
        """This allows for Grid visualisation"""
        if r_pos is None:
            r_pos = (self.size + 1, self.size + 1)
        if d_pos is None:
            d_pos = (self.size + 1, self.size + 1)

        output = "  "
        for j in range(self.size):
            output += f"| {j} "
        output += "| \n"
        output += (self.size * 4 + 4) * "-"
        output += "\n"

        for i in range(self.size):
            output += f"|{i}"
            for j in range(self.size):
                if (i, j) == r_pos:
                    output += "| R "
                elif (i, j) == d_pos:
                    output += "| D "
                else:
                    output += f"| {sign} "
            output += "| \n"
            output += (self.size * 4 + 4) * "-"
            output += "\n"
        if delay:
            input('')
        print(output)


class BattleGrid(Grid):

    def __init__(self, size=10):
        """ This initialises the battle grid class """
        super().__init__(size=size)

    def print_grid(self, sign='*', r1_pos=None, r2_pos=None, delay=False):
        """This allows for Grid visualisation"""
        if r1_pos is None:
            r1_pos = (self.size + 1, self.size + 1)
        if r2_pos is None:
            r2_pos = (self.size + 1, self.size + 1)

        output = "  "
        for j in range(self.size):
            output += f"|  {j}  "
        output += "|  \n"
        output += (self.size * 6 + 4) * "-"
        output += "\n"

        for i in range(self.size):
            output += f"|{i}"
            for j in range(self.size):
                if (i, j) == r1_pos:
                    output += "|  R1 "
                elif (i, j) == r2_pos:
                    output += "|  R2 "
                else:
                    output += f"|  {sign}  "
            output += "| \n"
            output += (self.size * 6 + 4) * "-"
            output += "\n"
        if delay:
            input('')
        print(output)



