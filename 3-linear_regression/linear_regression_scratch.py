import random 
import torch

import sys
import os
sys.path.append(os.getcwd())
import TSlib

def synthetic_data(w, b, num_examples):
    '''生成y=Xw+b+噪声'''
    X = torch.normal(0, 1, (num_examples, len(w)))
    y = torch.matmul(X, w) + b
    y += torch.normal(0, 0.001, y.shape)
    return X, y.reshape((-1, 1))


if __name__ == "__main__":
    true_w = torch.tensor([2, -3.4])
    true_b = 4.2
    features, labels = synthetic_data(true_w, true_b, 1000)
    TSlib.set_figsize()
    TSlib.plt.scatter(features[:, 1].detach().numpy(), labels.detach().numpy(), 1);
    TSlib.plt.show()
    
    
    