from robot import Robot

class LeapingRobot(Robot):
    def __init__(self,identifier,name,position,direction):
        super().__init__(identifier,name,position,direction)

    def move_forward(self,grid_size):
        print('Leaping forward.')
        if self.direction=='n':
            new_row=0
            new_row=max(0,new_row)
            self.position=(new_row,self.position[1])
        elif self.direction=='s':
            new_row=grid_size-1
            new_row=min(grid_size-1,new_row)
            self.position=(new_row,self.position[1])
        elif self.direction=='e':
            new_col=grid_size-1
            new_col=min(grid_size-1,new_col)
            self.position=(self.position[0],new_col)
        elif self.direction=='w':
            new_col=0
            new_col=max(0,new_col)
            self.position=(self.position[0],new_col)

        self._report_leap()

    def print_greeting(self):
        """ Prints my robot's name and id"""
        super().print_greeting()
        print(f'{self.name} is a leaping robot.')

    def _report_leap(self):
        print(f'I just jumped!')
