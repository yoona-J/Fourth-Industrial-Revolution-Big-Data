# 많이 팔린 음식은 무엇이고 몇개가 팔렸는지 확인

import pandas as pd

file_path = 'C:/Users/yoona/OneDrive/Desktop/4차산업혁명 빅데이터/6주차/chipotle.tsv'
chipo = pd.read_csv(file_path, sep = '\t')

# 정렬된 value에서 9번째까지만 가져와서 변수에 집어넣는다
item_count = chipo['item_name'].value_counts()[:10]
print(item_count)

# enumerate: index와 변수 값을 동시에 반복한다
# 따라서, idx-> index, val-> item name, cnt-> count 가 되므로 각 쌍을 동시에 roop하면서 반복한다.
# items() : 키와 값의 쌍을 다 가져옴
for idx, (val, cnt) in enumerate(item_count.items(), 1):
    print("Top", idx, ":", val, cnt)