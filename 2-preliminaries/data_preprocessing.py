import os

def create_data(dir = "data", file_name = "house_tiny.csv"):
    try:
        os.makedirs(os.path.join('.', dir), exist_ok=True)
    except:
        pass
    data_file = os.path.join('.', dir, file_name)
    with open(data_file, 'w') as f:
        f.write("NumRooms,Alley, Price\n")
        f.write("NA,Pave, 127500\n") # 每行表示一个数据样本
        f.write('2,NA, 106000\n')
        f.write('4,NA, 1781000\n')
        f.write('NA,NA, 140000\n')

def read_data_by_pandas(data_file):
    import pandas as pd
    data = pd.read_csv(data_file)
    print(data)
    return data


if __name__ == "__main__":
    import torch
    import pandas as pd
    dir = 'data'
    file_name = 'house_tiny.csv'
    file = os.path.join(dir, file_name)
    create_data(dir, file_name)
    data = read_data_by_pandas(file)
    inputs, outputs = data.iloc[:, 0:2], data.iloc[:, 2]
    print(inputs)
    inputs.iloc[:, 0] = inputs.iloc[:, 0].fillna(inputs.iloc[:, 0].mean())
    print(inputs)
    inputs = pd.get_dummies(inputs, dummy_na=True)
    print(inputs)
    X = torch.tensor(inputs.to_numpy(dtype=float))
    y = torch.tensor(outputs.to_numpy(dtype=float))
    print(X)
    print(y)

    