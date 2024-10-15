import numpy as np
import torch 
from torch import nn 
from torch.utils import data
from linear_regression_scratch import synthetic_data


def load_array(data_arrays, batch_size, is_train=True): 
    '''构造一个PyTorch数据迭代器'''
    dataset = data.TensorDataset(*data_arrays)
    return data.DataLoader(dataset, batch_size, shuffle=is_train)

if __name__ == "__main__":
    true_w = torch.tensor([2, -3.4])
    true_b = 4.2
    features, labels = synthetic_data(true_w, true_b, 1000)
    
    batch_size  = 10
    data_iter = load_array((features, labels), batch_size)
    
    print(next(iter(data_iter)))
    
    net = nn.Sequential(nn.Linear(2, 1))
    
    
    