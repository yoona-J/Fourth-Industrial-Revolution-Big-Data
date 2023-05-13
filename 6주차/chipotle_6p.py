import pandas as pd

file_path = 'C:/Users/yoona/OneDrive/Desktop/4차산업혁명 빅데이터/6주차/chipotle.tsv'
chipo = pd.read_csv(file_path, sep = '\t')

# order_id는 데이터 상 숫자의 의미가 아니기 때문에 str로 변환
chipo['order_id'] = chipo['order_id'].astype(str)

# Quantity 분포 확인
# chipo dataframe에서 수치형 피쳐들의 요약 통계량을 확인한다.
print(chipo.describe())

# order 당 메뉴가 몇개인지 확인
# order_id, item_name의 개수를 출력
# unique: 데이터에 고유값들이 어떤 종류가 있는지 알고 싶을 때 사용되는 함수
print(chipo['order_id'].unique())
print(chipo['order_id'].value_counts())