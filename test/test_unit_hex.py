import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))
from src.model.hex import Hex as Hex

def test_hex():
    a = Hex()
