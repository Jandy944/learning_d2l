import torch
import numpy as np
import sys


import os 
print("current path: {}".format(os.getcwd()))
sys.path.append(os.getcwd())
from TSlib.timer import Timer

if __name__ == "__main__":
    n = 10000
    a = torch.ones([n])
    b = torch.ones([n])
    c = torch.zeros([n])

    timer = Timer()
    for i in range(n):
        c[i] = a[i] + b[i]
    print(f'{timer.stop():.5f} sec')

    timer.start()
    d = a + b 
    print(f'{timer.stop():.5f} sec')