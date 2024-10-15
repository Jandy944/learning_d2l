#%matplotlib inline 

import numpy as np

import sys
import os
sys.path.append(os.getcwd())
import TSlib

if __name__ == "__main__":
    board = TSlib.ProgressBoard('x')
    for x  in np.arange(0, 10, 0.1):
        board.draw(x, np.sin(x), 'sin', every_n=2)
        board.draw(x, np.cos(x), 'cos', every_n=10)