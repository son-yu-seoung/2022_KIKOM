import pandas as pd
import os, time

if not os.path.exists('./excersize_info.csv'): # initialize
    excersize_df = pd.DataFrame({
        'Name' : 'admin',
        'Arm' : 0,
        'Leg' : 0,
        'Neck' : 0,
        'Finger' : 0,
        'Foot' : 0,
        'Eyes' : 0,
        'Ears' : 0,
        'Noise' : 0
    }, index=['0'])
    excersize_df.to_csv('./excersize_info.csv')

excersize_df = pd.read_csv('./excersize_info.csv', index_col = 0)

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
        target_name = str(input('수정할 사람의 이름을 입력해주세요'))
        target_location = excersize_df.index[excersize_df['Name'] == target_name]
        target_location = target_location.tolist()
        target_location = target_location[0]
        
        while True:
            print('\n============== 수정할 부위을 입력해주세요 ==============\n')
            body_select = int(input('0. Arm, 1. Leg, 2. Neck, 3. Finger, 4. Foot, 5. Eyes, 6. Ears, 7. Noise, 8. 종료'))
            
            if body_select == 0:
                change_value = int(input())
                excersize_df.at[target_location, 'Arm'] = change_value
            
            elif body_select == 1:
                change_value = int(input())
                excersize_df.at[target_location, 'Leg'] = change_value
            
            elif body_select == 2:
                change_value = int(input())
                excersize_df.at[target_location, 'Neck'] = change_value
            
            elif body_select == 3:
                change_value = int(input())
                excersize_df.at[target_location, 'Finger'] = change_value
            
            elif body_select == 4:
                change_value = int(input())
                excersize_df.at[target_location, 'Foot'] = change_value
            
            elif body_select == 5:
                change_value = int(input())
                excersize_df.at[target_location, 'Eyes'] = change_value
            
            elif body_select == 6:
                change_value = int(input())
                excersize_df.at[target_location, 'Ears'] = change_value
            
            elif body_select == 7:
                change_value = int(input())
                excersize_df.at[target_location, 'Noise'] = change_value
            
            elif body_select == 8:
                excersize_df.to_csv('./excersize_info.csv')
                print('종료하겠습니다.\n')
                time.sleep(2)
                break
        
    elif select == 3: # data delete
        print('\n==================== 데이터 삭제====================\n')
        target_name = str(input('수정할 사람의 이름을 입력해주세요.\n'))
        target_location = excersize_df.index[excersize_df['Name'] == target_name]
        target_location = target_location.tolist()
        target_location = target_location[0]
        
        excersize_df = excersize_df.drop([target_location])
        print(excersize_df)
        excersize_df.to_csv('./excersize_info.csv')

    elif select == 4: # exit the program
        print('\n==================== 프로그램 종료 ====================\n')
        print('종료하겠습니다.\n')
        time.sleep(2)
        break

    else: # except
        print('잘못된 입력을 하셨습니다.\n')
        continue 
