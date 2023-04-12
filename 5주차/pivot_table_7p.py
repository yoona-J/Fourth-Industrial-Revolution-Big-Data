import pandas as pd

df = pd.read_csv('C:/Users/yoona/OneDrive/Desktop/4차산업혁명 빅데이터/5주차/pivot_ex.xlsx')

# aggfunc default = mean
print(df.pivot_table(index = ['code'], columns=['product']))
print(df.pivot_table(index = ['code'], columns='product', aggfunc='sum'))
print(df.pivot_table(index = ['code'], columns='product', aggfunc='size'))