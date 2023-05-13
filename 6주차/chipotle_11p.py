# 많이 팔린 음식은 무엇이고 몇개가 팔렸는지 확인

import pandas as pd

file_path = 'C:/Users/yoona/OneDrive/Desktop/4차산업혁명 빅데이터/6주차/chipotle.tsv'
chipo = pd.read_csv(file_path, sep = '\t')

print(chipo['item_name'].unique())
# item_name의 키와 해당 값을 sorting해서 출력한다
print(chipo['item_name'].value_counts())
