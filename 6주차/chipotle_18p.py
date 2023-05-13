# 한 주문에 $15 이상 지불한 주문번호(id)

import pandas as pd

file_path = 'C:/Users/yoona/OneDrive/Desktop/4차산업혁명 빅데이터/6주차/chipotle.tsv'
chipo = pd.read_csv(file_path, sep = '\t')

chipo['item_price'] = chipo['item_price'].apply(lambda x: float(x[1:]))

chipo_orderid_group = chipo.groupby('order_id').sum()
print(chipo_orderid_group)

results = chipo_orderid_group[chipo_orderid_group.item_price >= 15]
print('------------------------')
print(results[:10])