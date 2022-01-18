# RNN를 위한 API는 torch.nn.RNN(*args, **kwargs)

# training data를 만들때 input  : 월(가슴), 화(어깨), 수(하체), 목(등), 금(유산소), output : 가슴 운동 명, ... 이라면
# input : 월(유산소), 화(하체), 수(어깨), 목(등), 금(가슴), output : 유산소 운동 명, ... <-- data augmentation

# 밑의 예제는 NLP(Natural Language Processing)을 위한 코드이다. 앞의 두 단어를 보고, 뒤에 나올 단어를 예측

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

sentences = ['i like dog', 'i love coffe', 'i hate milk', 'you like cat', 'you love mlik', 'you hate coffee']
dtype = torch.float

# Word Processing
word_list = list(set(" ".join(sentences).split()))
word_dict = {w: i for i, w in enumerate(word_list)}
number_dict = {i: w for i, w in enumerate(word_list)}
n_class = len(word_dict)


# TextRNN Parameter
batch_size = len(sentences)
n_step = 2 # 학습 하려고 하는 문장의 길이 - 1 <- why?
n_hidden = 5 # 은닉층 사이즈 

def make_batch(sentences):
    input_batch = []
    target_batch = []

    for sen in sentences:
        word = sen.split()
        input = [word_dict[n] for n in word[:-1]] # 앞의 두 단어
        target = word_dict[word[-1]] # 뒤의 한 단어

        input_batch.append(np.eye(n_class)[input]) # One-Hot Encoding 
        target_batch.append(target)

    return input_batch, target_batch

input_batch, target_batch = make_batch(sentences)
input_batch = torch.tensor(input_batch, dtype=torch.float32, requires_grad=True)
target_batch = torch.tensor(target_batch, dtype=torch.int64)

# TextRNN
class TextRNN(nn.Module):
    def __init__(self):
        super(TextRNN, self).__init__()

        self.rnn = nn.RNN(input_size=n_class, hidden_size=n_hidden, dropout=0.3)
        self.W = nn.Parameter(torch.randn([n_hidden, n_class]).type(dtype))
        self.b = nn.Parameter(torch.randn([n_class]).type(dtype))
        self.Softmax = nn.Softmax(dim=1) # 대문자 시작이 맞나..?

    def forward(self, hidden, X):
        X = X.transpose(0, 1)
        outputs, hidden = self.rnn(X, hidden)
        outputs = outputs[-1]  # 최종 예측 Hidden Layer
        model = torch.mm(outputs, self.W) + self.b  # 최종 예측 최종 출력 층
        return model

# Training
model = TextRNN()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

for epoch in range(500):
  hidden = torch.zeros(1, batch_size, n_hidden, requires_grad=True)
  output = model(hidden, input_batch)
  loss = criterion(output, target_batch)

  if (epoch + 1) % 100 == 0:
    print('Epoch:', '%04d' % (epoch + 1), 'cost =', '{:.6f}'.format(loss))
  
  optimizer.zero_grad()
  loss.backward()
  optimizer.step()

input = [sen.split()[:2] for sen in sentences]

hidden = torch.zeros(1, batch_size, n_hidden, requires_grad=True)
predict = model(hidden, input_batch).data.max(1, keepdim=True)[1]
print([sen.split()[:2] for sen in sentences], '->', [number_dict[n.item()] for n in predict.squeeze()])