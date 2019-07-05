import numpy as np
import subprocess as sp
import random
import time

# Sets up a class for the game
class Grid(object):
    def __init__(self,dimentions):
        self.dimentions = dimentions  # Games could be extended to larger dimentions in the future!
        self.grid = np.zeros((dimentions,dimentions))

    def get_grid_value(self,coords):
        assert(coords[0] <= self.dimentions)
        assert(coords[1] <= self.dimentions)
        assert(coords[0] >= 0)
        assert(coords[1] >= 0)
        value = self.grid[coords[0],coords[1]]
        return value

    def get_grid_symbol(self,coords):
        value = self.get_grid_value(coords)
        assert(value in [-1,0,1])
        if value == -1:
            return 'X'
        if value == 0:
            return ' '
        if value == 1:
            return 'O'

    def set_grid_value(self,coords,value):
        self.grid[coords[0],coords[1]] = value

    def print_game(self):
        print(' '+('-'*self.dimentions*4))
        for i in range(self.dimentions):
            running_row = ''
            for j in range(self.dimentions):
                running_row += (' | ' + self.get_grid_symbol([i,j]))
            print(running_row + ' |')
            print(' '+('-'*self.dimentions*4))

    def check_for_win(self):
        if self.dimentions in (list(self.grid.sum(axis=0))+list(self.grid.sum(axis=1))):
            return 'O Wins'
        elif self.dimentions in [self.grid.trace(),np.fliplr(self.grid).trace()]:
            return 'O Wins'
        elif (-self.dimentions) in (list(self.grid.sum(axis=0))+list(self.grid.sum(axis=1))):
            return 'X Wins'
        elif (-self.dimentions) in [self.grid.trace(),np.fliplr(self.grid).trace()]:
            return 'X Wins'
        else:
            return 'No Win'

    def check_for_stalemate(self):
        temp = np.ravel(self.grid)
        number_of_zeros = len(temp[temp==0])
        if number_of_zeros == 0:
            return True
        else:
            return False

def print_instructions(value):
    assert(value in [1,-1])
    if value == 1:
        print('Player O: choose your move')
    if value == -1:
        print('Player X: choose your move')

def print_letter_guide():
    lets = ['q','w','e','a','s','d','z','x','c']
    n = 0
    print(' '+('-'*3*4))
    for i in range(3):
        running_row = ''
        for j in range(3):
            running_row += (' | ' + lets[n].upper())
            n += 1
        print(running_row + ' |')
        print(' '+('-'*3*4))

# Function to provide the correspondence between letter input and coordinates on grid
def letter_to_coord(letter):
    if letter == 'q':
        return [0,0]
    elif letter == 'w':
        return [0,1]
    elif letter == 'e':
        return [0,2]
    elif letter == 'a':
        return [1,0]
    elif letter == 's':
        return [1,1]
    elif letter == 'd':
        return [1,2]
    elif letter == 'z':
        return [2,0]
    elif letter == 'x':
        return [2,1]
    elif letter == 'c':
        return [2,2]
    else:
        return []

def check_letter_valid(letter):
    if letter in ['q','w','e','a','s','d','z','x','c']:
        return True
    else:
        return False

if __name__ == '__main__':
    print('Welcome to tictactoe!')
    print('Ready player O?')
    print('')
    print('Press Enter to continue')
    raw_input()
    print('Press one of these letter keys then Enter to select these squares')
    print_letter_guide()
    print('Press Enter to start')
    raw_input()
    grid = Grid(3)
    player_value = 1
    while(grid.check_for_win() == 'No Win' and not grid.check_for_stalemate()):
        sp.call('clear', shell=True)
        grid.print_game()
        print_instructions(player_value)
        VALID_INPUT = False
        if player_value == 1:
            while(not VALID_INPUT):
                letter = raw_input('Select Square: ').lower()
                if(not check_letter_valid(letter)):
                    print('Invalid input. Please choose a valid letter.')
                    continue
                coords = letter_to_coord(letter)
                if(grid.get_grid_value(coords) != 0):
                    print('Position occupied. Choose another.')
                    continue
                VALID_INPUT = True
        else:
            avail_coords = np.argwhere(grid.grid==0)
            num_avail_coords = avail_coords.shape[0]
            index = random.randint(0,num_avail_coords-1)
            coords = avail_coords[index]
            time.sleep(0.3)

        grid.set_grid_value(coords,player_value)
        player_value *= -1  # Active player switches here

    if(grid.check_for_stalemate()):
        sp.call('clear', shell=True)
        grid.print_game()
        print('Sorry, the game is a stalemate!')
    else:
        sp.call('clear', shell=True)
        grid.print_game()
        print('Congratulations!')
        print(grid.check_for_win())
