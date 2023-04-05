import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('classic')

df = pd.read_csv('C:/Users/yoona/OneDrive/Desktop/4차산업혁명 빅데이터/4주차/auto-mpg.csv', header=None)
print(df)

# 열 이름 지정
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'accleration', 'model year',
              'origin', 'name']
# mpg(연비) 열에 대한 히스토그램 그리기
df['mpg'].plot(kind='hist', bins=10, color='coral', figsize=(10, 5))

# 히스토그램
plt.title('Histogram')
plt.xlabel('mpg')
plt.show()