import random
class grid:
    def __init__(self,size=10):
        """ This initialises the grid class """
        self.size=size
        

    def _get_end_position(self):
        """ Initialises a random end position for the robot in the square grid
        Args:
            grid_size (int)

        Returns:
            a 2 item list [row,column]"""

        
        row=random.choice([0,self.size-1])
        col=random.choice([0,self.size-1])
        return(row,col)

    def _get_position(self):
        """ Initialises a random position for the robot in the square grid
        Args:
            grid_size (int)

        Returns:
            a 2 item list [row,column]"""
    
        row=random.randint(0,self.size-1)
        col=random.randint(0,self.size-1)
        return (row,col)

    def _wall_test(self, position,direction):
        """ Checks whether the robot has hit the wall or not. Will return a boolean
        Args:
            row (int): The current row
            col (int): The current column
            direction (str): The current direction
            grid_size (int): The size of the square grid

        Returns:
            True/False if the robot is/isn't at the wall"""

        row = position[0]
        col = position[1]
        grid_size=self.size
        if direction == 'n' and row <= 0:
            return True
        elif direction=='s'and row>=grid_size-1:
            return True
        elif direction=='e'and col>=grid_size-1:
            return True
        elif direction=='w' and col<=0:
            return True
        else:
            return False
