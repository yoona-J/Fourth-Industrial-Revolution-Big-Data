import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('default')
df = pd.read_csv('C:/Users/yoona/OneDrive/Desktop/4차산업혁명 빅데이터/4주차/auto-mpg.csv', header=None)

# 열 이름 지정
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'accleration', 'model year',
              'origin', 'name']

# 한글 폰트
from matplotlib import font_manager, rc
font_path = 'C:/Windows/Fonts/NGULIM.TTF'
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

# 그래프 객체 생성
fig = plt.figure(figsize=(5, 10))
# 2개의 열, 1개의 행
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)

# axe 그래프에 boxplot 메서드로 그래프 출력
ax1.boxplot(x=[df[df['origin']==1]['mpg'],
               df[df['origin']==2]['mpg'],
               df[df['origin']==3]['mpg']],
               labels=['USA', 'EU', 'JAPAN'])

ax2.boxplot(x=[df[df['origin']==1]['mpg'],
               df[df['origin']==2]['mpg'],
               df[df['origin']==3]['mpg']],
               labels=['USA', 'EU', 'JAPAN'], vert=False) #vertical = False => 수평

ax1.set_title('제조국가별 연비 분포 (수직 박스 플롯)')
ax2.set_title('제조국가별 연비 분포 (수평 박스 플롯)')

plt.show()
