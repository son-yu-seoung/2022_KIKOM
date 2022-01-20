import numpy as np
import pandas as pd 
import pandas_datareader.data as pdr
import matplotlib.pyplot as plt

import datetime

import torch
import torch.nn as nn
from torch.autograd import Variable

import torch.optim as optim
from torch.utils.data import Dataset, DataLoader 

start = (2000, 1, 1)
start = datetime.datetime(*start)
end = datetime.date.today() 

df = pdr.DataReader('005930.KS', 'yahoo', start, end)
print(df.head(5))
print(df.tail(5))
df.Close.plot(grid=True)
# plt.show()

''' 
open : 시가
high : 고가
low : 저가
close : 종가
volume : 거래량
Adj Close : 주식의 분할, 배당, 배분 등을 고려해 조정한 종가
'''

x = df.drop(columns='Volume') # 왜 x 데이터에 adj close를 삭제 안했지?
y = df.iloc[:, 5:6]
print(x)
print(y)

# 학습을 위한 데이터 정규화
# StandardScaler : 각 특징의 평균을 0, 분산을 1이 되도록 변경
# MinMaxScaler : 최대최소값이 각각 1, 0이 되도록 변경

from sklearn.preprocessing import StandardScaler, MinMaxScaler

mm = MinMaxScaler()
ss = StandardScaler()

x_ss = ss.fit_transform(x)
y_mm = mm.fit_transform(y)

# training data
train_x = x_ss[:4500, :]
train_y = y_mm[:4500, :]

# test data
test_x = x_ss[4500:, :]
test_y = y_mm[4500:, :]

print('Training Shape', train_x.shape, train_y.shape)
print('Testing Shape', test_x.shape, test_y.shape)

'''
torch Variable에는 3개의 형태가 있다.
data, grad, grad_fn 
'''
train_x_tensors = Variable(torch.Tensor(train_x))
train_y_tensors = Variable(torch.Tensor(train_y))

test_x_tensors = Variable(torch.Tensor(test_x))
test_y_tensors = Variable(torch.Tensor(test_y))

# (4500, 5) -> [4500, 1, 5] why?
train_x_tensors_final = torch.reshape(train_x_tensors, (train_x_tensors.shape[0], 1, train_x_tensors.shape[1]))
test_x_tensors_final = torch.reshape(test_x_tensors, (test_x_tensors.shape[0], 1,test_x_tensors.shape[1]))

print('tensor shape', train_x_tensors_final.shape, train_y_tensors.shape)
print('tensor shape', test_x_tensors_final.shape, test_y_tensors.shape)

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu') # device

class LSTM(nn.Module):
    def __init__(self, num_classes, input_size, hidden_size, num_layers, seq_length):
        super(LSTM, self).__init__()

        self.num_classes = num_classes
        self.num_layers = num_layers
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.seq_length = seq_length

        self.lstm = nn.LSTM(input_size=input_size, hidden_size=hidden_size,
                            num_layers=num_layers, batch_first=True)
        self.fc_1 = nn.Linear(hidden_size, 128)
        self.fc = nn.Linear(128, num_classes)

        self.relu = nn.ReLU()

    def forward(self, x):
        pass
