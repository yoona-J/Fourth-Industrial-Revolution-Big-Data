# y축이 두개인 막대 선 그래프

import pandas as pd
import matplotlib.pyplot as plt
# critical error만 나타나도록
import warnings
warnings.simplefilter("ignore")

# excel 데이터를 데이터프레임으로 변환
# excel이나 csv로 읽을 때는 어디가 header인지 명시 필요
file_path = 'C:/Users/yoona/OneDrive/Desktop/4차산업혁명 빅데이터/4주차/남북한발전전력량.xlsx'
# convert_float=True -> 숫자데이터를 float로
df = pd.read_excel(file_path, engine='openpyxl', header=0, convert_float=True)
print(df)

df = df.loc[5:9]
df.drop('전력량 (억㎾h)', axis='columns', inplace=True)
df.set_index('발전 전력별', inplace=True)
print(df)
df = df.T #transpose
print(df)

# 증감율(변동률) 계산
df = df.rename(columns={'합계':'총발전량'})
df['총발전량 - 1년'] = df['총발전량'].shift(1)
df['증감율'] = ((df['총발전량'] / df['총발전량 - 1년']) - 1) * 100

# 한글 폰트 설정
from matplotlib import font_manager, rc
font_path = 'C:/Windows/Fonts/NGULIM.TTF'
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

# 2축 그래프
ax1 = df[['수력', '화력']].plot(kind='bar', figsize=(20, 10), width=0.7, stacked=True)

# twinx -> ax1 x축을 똑같이 가져온다
ax2 = ax1.twinx()
ax2.plot(df.index, df.증감율, linestyle='--', marker='o', markersize=20,
         color='green', label='전년대비 증감율(%)')
ax1.set_ylim(0, 500)
ax2.set_ylim(-50, 50)

ax1.set_xlabel('연도', size=20)
ax1.set_ylabel('발전량 (억㎾h)')
ax2.set_ylabel('전년 대비 증감율(%)')

plt.title('북한 전력 발전량 (1990-2016)', size=30)
ax1.legend(loc='upper left')

plt.show()