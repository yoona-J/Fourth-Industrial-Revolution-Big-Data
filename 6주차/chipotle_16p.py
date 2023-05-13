# 아이템 별 주문 개수와 총량

import pandas as pd

file_path = 'C:/Users/yoona/OneDrive/Desktop/4차산업혁명 빅데이터/6주차/chipotle.tsv'
chipo = pd.read_csv(file_path, sep = '\t')

# item 당 주문 개수 - count()
# item_name과 order_id를 그룹화
order_count = chipo.groupby('item_name')['order_id'].count()
print(order_count[:10])

# item 당 주문 총량 - sum()
# item_name과 quantity를 그룹화
item_quantity = chipo.groupby('item_name')['quantity'].sum()
print('------------------------------')
print(item_quantity[:10])