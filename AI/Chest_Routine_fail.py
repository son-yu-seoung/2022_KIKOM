import pandas as pd
import numpy as np

from numpy import array
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Dense, LSTM, Input, Dropout, add, Embedding

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical

# 버전 : 2022-01-26
# 추가해야할 것 : target 값에 token을 넣어야하는데 어떤 shape로 넣어야할 지 공부가 필요 

class Excersize_LSTM:
    def __init__(self):
        self.user_parameter_len = 7
        self.max_length = 5 # 루틴에 존재하는 운동의 개수
        self.vocab_size = 7 # 단어의 수 (중복 X)
        self.embedding_dim = 16 # choice

        self.Start = 'startseq'
        self.End = 'endseq'

        self.epoch = 10
        
    def load_data(self):
        df_x = pd.read_excel('./dataset/가슴/data_x.xlsx')
        df_y = pd.read_excel('./dataset/가슴/data_y.xlsx')

        # dataset create 
        data_x, data_y = list(), list()

        for i in range(len(df_x)): # not clean
            temp = list()
            
            temp.append(df_x.iloc[i]['다이어트'])
            temp.append(df_x.iloc[i]['운동 개수'])
            temp.append(df_x.iloc[i]['수준'])
            temp.append(df_x.iloc[i]['기구 유무'])
            temp.append(df_x.iloc[i]['근성장'])
            temp.append(df_x.iloc[i]['벌크업'])
            temp.append(df_x.iloc[i]['다이어트'])

            data_x.append(temp) # (n, 7)

        for i in range(len(df_y)): # not clean
            data_y.append(str(df_y.iloc[i]['운동1'])+' '+ 
                        str(df_y.iloc[i]['운동2'])+' '+
                        str(df_y.iloc[i]['운동3'])+' '+
                        str(df_y.iloc[i]['운동4'])+' '+
                        str(df_y.iloc[i]['운동5']))

        print('data_x', data_x)
        print('data_y', data_y)

        return data_x, data_y

    def pre_processing(self, data_x, data_y):
        tokenizer = Tokenizer()
        tokenizer.fit_on_texts(data_y)
        sequences = tokenizer.texts_to_sequences(data_y)

        print('정수 인코딩 :', sequences)

        word_index = tokenizer.word_index

        print('단어에 맵핑된 정수값 :', word_index)

        sequences = pad_sequences(sequences, maxlen=5) # 5개 종류의 운동 
        
        self.vocab_size = len(tokenizer.word_index) + 1

        target = np.array([0, 1, 2, 3, 4, 5, 6])
        target = to_categorical(target)
        print(target[0])


        return data_x, np.array(sequences), target

        # # 정수 인코딩
        # tokenizer = Tokenizer()
        # for routine in data_y: # ['푸쉬업' '벤치프레스' '랫풀다운' 'nan' 'nan']
        #     for each_name in routine: # '푸쉬업', '벤치프레스', '랫풀다운', 'nan', 'nan'
        #         tokenizer.fit_on_texts([each_name])

        # tokenizer.fit_on_texts(['start'])
        # tokenizer.fit_on_texts(['end'])

        # for routine in data_y:
        #     temp = list()
        #     for each_name in routine:
        #         temp.append(tokenizer.texts_to_sequences([each_name])[0][0])
        #     sequences.append(temp)

        # print('단어 집합 : ', tokenizer.word_index)
        # print('정수 인코딩 : ', sequences)

        # train_x_user = np.array(data_x) # 나중엔 train, test split
        # train_x_data = np.array(sequences)

        # target = np.array([[3, 4, 1, 1, 9], [6, 7, 2, 1, 9]]) # 9 is 'end'

        # return train_x_user, train_x_data, target

    def model(self):
        input1 = Input(shape=(self.user_parameter_len,))
        fe1 = Dropout(0.5)(input1)
        fe2 = Dense(256, activation='relu')(fe1)

        input2 = Input(shape=(self.max_length,)) # 5
        se1 = Embedding(self.vocab_size, self.embedding_dim, input_length=5)(input2) # (1)
        se2 = Dropout(0.5)(se1)
        se3 = LSTM(256)(se2)

        decoder1 = add([fe2, se3])
        decoder2 = Dense(256, activation='relu')(decoder1)
        output = Dense(self.vocab_size, activation='softmax')(decoder2)

        return Model(inputs=[input1, input2], outputs=[output])

    def train(self, train_x_user, train_x_data, target):
        model = self.model()
        model.summary()
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['acc'])

        for i in range(1):#(self.epoch):
            model.train_on_batch([train_x_user[0][0], train_x_data[0]], target[0])
            model.train_on_batch([train_x_user[1][0], train_x_data[1]], target[1])

    def start(self):
        data_x, data_y = self.load_data()
        train_x_user, train_x_data, target = self.pre_processing(data_x, data_y)
        self.train(train_x_user, train_x_data, target)

p_object = Excersize_LSTM()
p_object.start()
        

    
# # captionModel.layers[2].set_weights([embedding_matrix])
# # captionModel.layers[2].trainable = False
# # captionModel.compile(loss='categorical_crossentropy', optimizer='adam')


