from ttt import *

def test_grid_value():
    grid = Grid(3)
    value = grid.get_grid_value([0,0])
    assert value == 0

def test_grid_symbol():
    grid = Grid(3)
    grid.set_grid_value([0,0],1)
    grid.set_grid_value([0,1],-1)
    symb1 = grid.get_grid_symbol([0,0])
    symb2 = grid.get_grid_symbol([0,1])
    assert symb1 == 'O'
    assert symb2 == 'X'

def test_check_win():
    grid = Grid(3)
    grid.set_grid_value([0,0],1)
    grid.set_grid_value([1,0],1)
    grid.set_grid_value([2,0],1)
    assert grid.check_for_win() == 'O Wins'
