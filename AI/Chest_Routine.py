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
# notion : 이것은 원래 계획의 down version

class Chest_Routine:
    def __init__(self):
        self.path = Hparams_Chest_Routine['path']

        self.max_length = Hparams_Chest_Routine['max_length']
        self.vocab_size = Hparams_Chest_Routine['vocab_size']
        self.embedding_dim = Hparams_Chest_Routine['embedding_dim']

        self.epoch = Hparams_Chest_Routine['epochs']
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
            data_routine.append(str(df_routine.iloc[i]['운동1'])+' '+ 
                        str(df_routine.iloc[i]['운동2'])+' '+
                        str(df_routine.iloc[i]['운동3'])+' '+
                        str(df_routine.iloc[i]['운동4'])+' '+
                        str(df_routine.iloc[i]['운동5']))

        print('data_x', data_user)
        print('data_y', data_routine)

        return data_user, data_routine

    def pre_processing(self, data_user, data_routine):
        tokenizer = Tokenizer()
        tokenizer.fit_on_texts(data_routine)
        data_routine = tokenizer.texts_to_sequences(data_routine)

        sequences = list()
        for i in range(0, len(data_routine)):
            for j in range(1, len(data_routine[i])):
                if len(data_routine[i]) > 1:
                    sequence = data_routine[i][j-1:j+1]
                    sequences.append(sequence)

        sequences = np.array(sequences)

        train_x_routine, train_y_routine = sequences[:,0], sequences[:,1]
        train_y_routine = to_categorical(train_y_routine, num_classes=self.vocab_size)

        self.train_x_routine, self.test_x_routine, self.train_y_routine, self.test_y_routine = train_test_split(train_x_routine, train_y_routine, test_size=0.2, random_state=777)

        return 0

    def model(self):
        model = Sequential()

        model.add(Embedding(self.vocab_size, self.embedding_dim, input_length=1)) # 
        model.add(LSTM(10)) # 
        model.add(Dense(self.vocab_size, activation='softmax'))

        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        model.summary()

        return model

    def train(self):
        model = self.model()

        model.fit(self.train_x_routine, self.train_y_routine, epochs=10, verbose=2)
        pred = model.predict(self.test_x_routine)

        print(pred)

        return 0 
            
    def start(self):
        data_user, data_routine = self.load_data(self.path)
        self.pre_processing(data_user, data_routine) # create train, test set
        self.train()

c_object = Chest_Routine()
c_object.start()
        


