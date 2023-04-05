# 서울에서 경기도로 이동한 인구데이터를 그려본다.

import pandas as pd
import matplotlib.pyplot as plt
# critical error만 나타나도록
import warnings
warnings.simplefilter("ignore")

# excel 데이터를 데이터프레임으로 변환
# excel이나 csv로 읽을 때는 어디가 header인지 명시 필요
file_path = 'C:/Users/yoona/OneDrive/Desktop/4차산업혁명 빅데이터/4주차/inoutpeople.xlsx'
df = pd.read_excel(file_path, engine='openpyxl', header=0)

# 병합된 줄(NaN)을 해당 열의 앞 데이터로 채운다.
df = df.fillna(method='ffill')

# 서울에서 다른 지역으로 이동한 데이터만 추출
mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')

# true인 부분만 df_seoul로 저장한다. (서울에서 다른 지역으로 전출하는 데이터) -> boolean indexing
df_seoul = df[mask]

# axis=1 : 열 / axis=0 : 행
# 전출지별 열을 없앤다
df_seoul = df_seoul.drop(['전출지별'], axis=1)

# inplace=True 가 없으면 해당 줄에서만 적용되고 다음 줄에서는 적용되지 않기 때문에 꼭 넣어준다.
# inplace를 사용하지 않을 거라면 변수로 설정해서 넣어준다.
df_seoul.rename({'전입지별':'전입지'}, axis=1, inplace=True)

# 전입지로 인덱스 변경
df_seoul.set_index('전입지', inplace=True)

# loc = 열 선택
# 경기도 인구값만 가져오기
sr_one = df_seoul.loc['경기도']
print(sr_one)

# 선그래프
plt.style.use('ggplot')
plt.figure(figsize=(14, 5))
plt.xticks(size=10, rotation='vertical')

plt.plot(sr_one.index, sr_one.values, marker='o', markersize=10)
plt.title('Seoul -> Gyeonggi population flow')
plt.xlabel('Period')
plt.ylabel('# of population')
plt.show()


# 첫 10줄만 읽어오기
print(df.head(10))