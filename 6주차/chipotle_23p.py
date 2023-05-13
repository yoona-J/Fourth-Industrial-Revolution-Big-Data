# 가장 비싼 주문에서는 총 몇 개의 음식이 팔렸을까

import pandas as pd

file_path = 'C:/Users/yoona/OneDrive/Desktop/4차산업혁명 빅데이터/6주차/chipotle.tsv'
chipo = pd.read_csv(file_path, sep = '\t')

chipo['item_price'] = chipo['item_price'].apply(lambda x: float(x[1:]))

# order_id를 기준으로 그룹화 한 것을 quantity 개수를 합치고 item_price가 높은 순으로 sorting 한 후 상위 5개만 나타낸다.
rst = chipo.groupby('order_id').sum().sort_values(by = 'item_price', ascending=False)[:5]
print(rst)