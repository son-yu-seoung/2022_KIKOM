from unittest.util import _MAX_LENGTH
import pandas as pd
import numpy as np

from numpy import array
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Dense, LSTM, Input, Dropout, add, Embedding

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical

from sklearn.model_selection import train_test_split
from Hparams import *

# 버전 : 2022-01-29
# notion : 현재 trani set에 대해서도 정확히 예측 못함 문제 원인 찾기 (data 수, 숫자 예측의 허점 등)

class Chest_Routine:
    def __init__(self):
        self.path = Hparams_Chest_Routine['path']

        self.max_length = Hparams_Chest_Routine['max_length']
        self.vocab_size = Hparams_Chest_Routine['vocab_size']
        self.embedding_dim = Hparams_Chest_Routine['embedding_dim']

        self.epochs = Hparams_Chest_Routine['epochs']
        self.loss = Hparams_Chest_Routine['loss']
        self.optimizer = Hparams_Chest_Routine['optimizer']
        
    def load_data(self, path):
        df_user = pd.read_excel(path+'user.xlsx')
        df_routine = pd.read_excel(path+'routine.xlsx')

        # dataset create 
        data_user, data_routine = list(), list()

        for i in range(len(df_user)): # not clean
            temp = list()
            
            temp.append(df_user.iloc[i]['다이어트'])
            temp.append(df_user.iloc[i]['운동 개수'])
            temp.append(df_user.iloc[i]['수준'])
            temp.append(df_user.iloc[i]['기구 유무'])
            temp.append(df_user.iloc[i]['근성장'])
            temp.append(df_user.iloc[i]['벌크업'])
            temp.append(df_user.iloc[i]['다이어트'])

            data_user.append(temp) # (n, 7)

        for i in range(len(df_routine)): # not clean
            data_routine.append('시작' + ' ' + # input에 시작 추가
                        str(df_routine.iloc[i]['운동1'])+' '+ 
                        str(df_routine.iloc[i]['운동2'])+' '+
                        str(df_routine.iloc[i]['운동3'])+' '+
                        str(df_routine.iloc[i]['운동4'])+' '+
                        str(df_routine.iloc[i]['운동5']))

        return data_user, data_routine

    def pre_processing(self, data_user, data_routine):
        self.tokenizer = Tokenizer()
        self.tokenizer.fit_on_texts(data_routine)
        self.tokenizer.fit_on_texts(['종료'])
        input = self.tokenizer.texts_to_sequences(data_routine)

        print(self.tokenizer.index_word)

        # 내가 직접 코딩하기 
        target = list()

        for seq in input:
            temp = list()

            for i in range(self.max_length):
                if i == self.max_length - 1:
                    temp.append(15)
                else:
                    temp.append(seq[i+1])

            target.append(temp)
         
        # train_x_routine, train_y_routine = sequences[:,0], sequences[:,1]
        
        # print(train_x_routine) 
        # print(train_y_routine) 
        # train_y_routine = to_categorical(train_y_routine, num_classes=self.vocab_size)

        train_x_routine, test_x_routine, train_y_routine, test_y_routine = train_test_split(input, target, shuffle=True, test_size=0.2)
        self.train_x_routine, self.test_x_routine, self.train_y_routine, self.test_y_routine = np.array(train_x_routine), np.array(test_x_routine), np.array(train_y_routine), np.array(test_y_routine)
        print(len(self.train_x_routine))
        print(len(self.test_x_routine))

        return 0

    def model(self):
        model = Sequential()

        model.add(Embedding(self.vocab_size, self.embedding_dim, input_length=1)) # 
        model.add(LSTM(32, input_shape=(6,1))) # LSTM(20, input_shape=(12,1)) time step, feature
        model.add(Dense(1)) # 각각 1개씩

        model.compile(loss=self.loss, optimizer=self.optimizer, metrics=['accuracy'])
        model.summary()

        return model

    def train(self):
        model = self.model()
        # predict 설정해야함 
        for i in range(self.epochs):
            print(f'{i+1} Epochs..')
            for j in range(len(self.train_x_routine)):
                model.train_on_batch(self.train_x_routine[j], self.train_y_routine[j])

        for i in range(len(self.test_x_routine)):
            pred = np.round(model.predict(self.train_x_routine[i]))
            print('정답 :', self.train_y_routine[i])
            print(f'예측 : {pred[0]} {pred[1]} {pred[2]} {pred[3]} {pred[4]} {pred[5]}') 

        return 0 
            
    def start(self):
        data_user, data_routine = self.load_data(self.path)
        self.pre_processing(data_user, data_routine) # create train, test set
        self.train()

c_object = Chest_Routine()
c_object.start()
        


