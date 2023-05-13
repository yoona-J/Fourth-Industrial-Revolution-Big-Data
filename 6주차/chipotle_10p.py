# item_price 분포 확인

import pandas as pd

file_path = 'C:/Users/yoona/OneDrive/Desktop/4차산업혁명 빅데이터/6주차/chipotle.tsv'
chipo = pd.read_csv(file_path, sep = '\t')

# 함수 정의 구문 def를 이용해 함수를 정의한다.
# $ 표시를 없애기 위해 x 값의 1번째부터 float으로 변환한다.
def splt_firstchar(x):
    return float(x[1:])

print(chipo.describe())
# $ 표시를 없애기 위해 lambda 함수 사용
# apply를 이용해 chipo['item_price']의 값에 일괄적으로 적용시킨다.
# apply(splt_firstchar)로 사용할 수도 있다.

chipo['item_price'] = chipo['item_price'].apply(lambda x: float(x[1:]))
print(chipo.describe())