# 각 아이템의 가격 확인

import pandas as pd

file_path = 'C:/Users/yoona/OneDrive/Desktop/4차산업혁명 빅데이터/6주차/chipotle.tsv'
chipo = pd.read_csv(file_path, sep = '\t')

chipo['item_price'] = chipo['item_price'].apply(lambda x: float(x[1:]))

# 각 아이템의 가격 계산
pd.set_option('display.max_columns', None)
# 동일 아이템을 1개만 구매한 주문만 선별한다
chipo_one_item = chipo[chipo.quantity == 1]
print(chipo_one_item)
print('++++++++++++++++++++++++++++++++++++++')
# item_name을 기준으로 그룹화를 하고 min()으로 최저가 계산
price_per_item = chipo_one_item.groupby('item_name').min()
print(price_per_item[:10])
print('=======================================')
# item_price를 기준으로 정렬
price_per_item.sort_values(by = "item_price", ascending= False)[:10]