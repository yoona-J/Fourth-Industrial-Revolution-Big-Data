import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('default')
df = pd.read_csv('C:/Users/yoona/OneDrive/Desktop/4차산업혁명 빅데이터/4주차/auto-mpg.csv', header=None)

# 열 이름 지정
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'accleration', 'model year',
              'origin', 'name']

# 데이터 개수 카운트를 위해 값 1을 가진 열 추가
df['count'] = 1
# origin 열을 중심으로 그룹화 후 합계 더하기
df_origin = df.groupby('origin').sum()
print(df_origin.head())

# origin 값 변경
df_origin.index = ['USA', 'EU', 'JAPAN']

# count 열을 사용해서 plot 그리기
df_origin['count'].plot(kind='pie', figsize=(7, 5), autopct='%1.1f%%',
                        colors=['chocolate', 'bisque', 'cadetblue'])

plt.title('Model Origin', size=20)
# 원으로 만들기 위해 비율을 같게 조정
plt.axis('equal')
plt.legend(labels=df_origin.index, loc='upper right')
plt.show()