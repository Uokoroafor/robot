import math
import random

name=input('What is the name of your Robot?')
identifier='Ten06'
age='32'
grid_size=10
#row=int(input('What is the row coordinate?'))
#col=int(input('What is the column coordinate?'))

row=int((random.sample(range(grid_size),1))[0])
col=int((random.sample(range(grid_size),1))[0])
direction=input('What is its initial direction [n|s|e|w]?')

row = min(grid_size-1,row)
row = max(row, 0)
col = min(grid_size-1,col)
col = max(col, 0)

row1=row
col1=col


if direction=='n':
    #fin_row=0
    #fin_col=col
    cardinal='North'
elif direction=='s':
    #fin_row=grid_size-1
    #fin_col=col
    cardinal='South'
elif direction=='e':
    #fin_row=row
    #fin_col=grid_size-1
    cardinal='East'
elif direction=='w':
    #fin_row=row
    #fin_col=0
    cardinal='West'

print(f'Hello my name is {name}. My ID is {identifier} and I am {age} years old!')
print(f'My current location is ({row},{col}), facing {cardinal}.')

while (col1!=grid_size-1) or (row1!=grid_size-1):
    wall=False
    while not wall:
        if direction=='n':
            row1-=1
            if row1<=0:
                wall=True
        elif direction=='s':
            row1+=1
            if row1>=grid_size-1:
                wall=True
        elif direction=='e':
            col1+=1
            if col1>=grid_size-1:
                wall=True
        elif direction=='w':
            col1-=1
            if col1<=0:
                wall=True

        print('Moving one step forward.')
        print(f'My current location is ({row1},{col1}), facing {cardinal}')
        
    print('I have a wall in front of me!')
    print('Turning 90 degrees clockwise.')
    if direction=='n':
        cardinal='East'
        direction='e'
    elif direction=='s':
        cardinal='West'
        direction='w'
    elif direction=='e':
        cardinal='South'
        direction='s'
    elif direction=='w':
        cardinal='North'
        direction='n'

print('I am now drinking Ribena and happy!')
