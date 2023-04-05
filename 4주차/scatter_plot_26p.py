import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('default')
df = pd.read_csv('C:/Users/yoona/OneDrive/Desktop/4차산업혁명 빅데이터/4주차/auto-mpg.csv', header=None)

# 열 이름 지정
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'accleration', 'model year',
              'origin', 'name']
# cylinders 개수의 상대적 비율을 계산하여 시리즈 생성
cylinders_size = df.cylinders / df.cylinders.max() * 300

df.plot(kind='scatter', x='weight', y='mpg', marker='+',
        figsize=(10, 5), cmap='viridis', c=cylinders_size, s=50, alpha=0.3)
plt.title('Scatter plot - mpg-weight-cylinders')
plt.show()