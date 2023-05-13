# 주문 당 평균 계산 금액

import pandas as pd

file_path = 'C:/Users/yoona/OneDrive/Desktop/4차산업혁명 빅데이터/6주차/chipotle.tsv'
chipo = pd.read_csv(file_path, sep = '\t')

chipo['item_price'] = chipo['item_price'].apply(lambda x: float(x[1:]))

checksum = chipo.groupby('order_id')['item_price'].sum()
checkmean = chipo.groupby('order_id')['item_price'].sum().mean()

print(checksum)
print('-----------------------------')
print(checkmean)