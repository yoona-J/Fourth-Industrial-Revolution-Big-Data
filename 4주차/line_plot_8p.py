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

plt.style.use('ggplot')

# 선그래프 두개 제작
fig = plt.figure(figsize=(10, 10))
ax1 = fig.add_subplot(2, 1, 1) # 2x1로 나누고, 1번 칸
ax2 = fig.add_subplot(2, 1, 2) # 2x1로 나누고, 2번 칸

ax1.plot(sr_one, 'o', markersize=10)
ax2.plot(sr_one, marker='o', markerfacecolor='green', markersize=10,
         color='olive', linewidth=2, label='Seoul - geonggi')
ax2.legend(loc='best')

# y축 범위 지정
ax1.set_ylim(50000, 800000)
ax2.set_ylim(50000, 800000)

# x축 라벨 지정 및 회전
ax1.set_xticklabels(sr_one.index, rotation=75)
ax2.set_xticklabels(sr_one.index, rotation=75)

ax1.set_xlabel('Period', size=20)
ax1.set_ylabel('Population flow', size=20)
ax2.set_xlabel('Period', size=12)
ax2.set_ylabel('Population flow', size=12)

ax1.tick_params(axis="x", labelsize=15)
ax1.tick_params(axis="y", labelsize=15)
ax2.tick_params(axis="x", labelsize=5)
ax2.tick_params(axis="y", labelsize=5)

plt.show()