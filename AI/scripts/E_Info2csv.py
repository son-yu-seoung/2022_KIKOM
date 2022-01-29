import pandas as pd
import os, time

if not os.path.exists('../dataset/가슴/data_x_1.csv'): # initialize
    excersize_df = pd.DataFrame({
        '운동 개수' : 3,
        '수준' : 2,
        '기구 유무' : 0,
        '근성장' : 1,
        '벌크업' : 0,
        '다이어트' : 0
    }, index=['0'])
    excersize_df.to_csv('../dataset/가슴/data_x_1.csv')

excersize_df = pd.read_csv('../dataset/가슴/data_x_1.csv', index_col = 0)

while True:
    time.sleep(2) # rest time

    insert_dict = dict()
    
    print('\n==================== 작업 선택 ====================\n')
    select = int(input('0. 확인, 1. 입력, 2. 수정, 3. 삭제, 4. 종료 : '))
    print()

    if select == 0: # data check
        print('\n==================== 데이터 확인 ====================\n')
        print(excersize_df)

    elif select == 1: # data insert
        print('\n==================== 데이터 입력 ====================\n')
        try:
            for i in excersize_df.columns[:]:
                if i == 'Name': 
                    insert_dict[i] = input('%s(str) : '%i) # str

                else: 
                    insert_dict[i] = int(input('%s(int) : '%i)) # int
            
            excersize_df = excersize_df.append(insert_dict, ignore_index=True)
            excersize_df.to_csv('./excersize_info.csv')
        
        except:
            print("\n예외 발생 (data type)")

    elif select == 2: # data retouch
        print('\n==================== 데이터 수정 ====================\n')
        pass

    elif select == 3: # data delete
        print('\n==================== 데이터 삭제====================\n')
        pass

    elif select == 4: # exit the program
        print('\n==================== 프로그램 종료 ====================\n')
        print('종료하겠습니다.\n')
        time.sleep(2)
        break

    else: # except
        print('잘못된 입력을 하셨습니다.\n')
        continue 
