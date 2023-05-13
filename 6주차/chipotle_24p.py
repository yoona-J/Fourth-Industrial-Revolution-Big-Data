# 'veggie salad bowl'이 몇 번 주문되었을까

import pandas as pd

file_path = 'C:/Users/yoona/OneDrive/Desktop/4차산업혁명 빅데이터/6주차/chipotle.tsv'
chipo = pd.read_csv(file_path, sep = '\t')
pd.set_option('display.max_columns', None)

chipo_salad = chipo[chipo['item_name'] == "Veggie Salad Bowl"]
print(len(chipo_salad))
print(chipo_salad.head(5))