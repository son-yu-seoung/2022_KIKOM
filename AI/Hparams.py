# 버전 2022-01-29

Hparams_Chest_Routine = {
    'path' : './dataset/가슴/',
    'max_length' : 5, # 가장 운동이 많은 루틴(띄어쓰기 개수로 구분)
    'vocab_size' : 8, # dataset에 나오는 운동의 수 + 1(중복 X, nan 포함)
    'embedding_dim' : 16, # word embedding의 hidden dimension

    'epochs' : 10,
    'loss' : 'categorical_crossentropy',
    'optimizer' : 'adam'
}