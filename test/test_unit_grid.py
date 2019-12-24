import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))
from src.model.grid import Grid as Grid

def test_grid():
    a = Grid()
