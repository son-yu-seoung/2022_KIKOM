import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt


body_data = pd.read_csv("./bodyperformance.csv")

body_data = body_data.drop(['Unnamed: 0'],axis = 1)
print(body_data.head(20))

for i in body_data.columns[:]:
    print(i)
# boon_muscle = 

