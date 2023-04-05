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

# 서울에서 '충청남도', '경상북도', '강원도'로 이동한 인구 데이터
df_3 = df_seoul.loc[['충청남도', '경상북도', '강원도']]

plt.style.use('ggplot')

fig = plt.figure(figsize=(20, 5))
ax = fig.add_subplot(1, 1, 1)

# 1970~2017 행을 string으로 변환하여 매핑
col_years = list(map(str, range(1970, 2018)))
# [:] -> 처음부터 끝까지(1970~2017) 다 나타낸다
ax.plot(col_years, df_3.loc['충청남도', :], marker='o', markerfacecolor='green',
        markersize=10, color='olive', linewidth=2, label='Seoul -> Chungnam')
ax.plot(col_years, df_3.loc['경상북도', :], marker='o', markerfacecolor='blue',
        markersize=10, color='skyblue', linewidth=2, label='Seoul -> Gyeongbuk')
ax.plot(col_years, df_3.loc['강원도', :], marker='o', markerfacecolor='red',
        markersize=10, color='magenta', linewidth=2, label='Seoul -> Gangwon')

# 범례 표시
ax.legend(loc='best')

ax.set_title('Seoul -> Chungnam, Gyeongnam, Gangwon population flow', size=20)

ax.set_xlabel('period', size=12)
ax.set_ylabel('population flow', size=12)

ax.set_xticklabels(col_years, rotation=90)

ax.tick_params(axis="x", labelsize=10)
ax.tick_params(axis="y", labelsize=10)

plt.show()
## 분석
# 지리적으로 가까운 충남 지역으로 이동한 인구가 다른 두 지역에 비해 많은 편이다.
# 전반적으로 1970~1980년대에는 서울에서 지방으로 전출하는 인구가 상대적으로 많은 편이다.
# 1990년댜 이후부터는 지방 전출이 줄었다.