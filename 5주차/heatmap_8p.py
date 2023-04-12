import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')

sns.set_style('darkgrid')

# 피벗테이블로 범주형 변수를 행과 열로 재구분
table = titanic.pivot_table(index=['sex'], columns=['class'], aggfunc='size')
print(table)

# make heatmap
sns.heatmap(table,               # table 데이터 사용
            annot=True, fmt='d', # 데이터 값 표시 여부 / 정수형 포맷 설정
            cmap='YlGnBu',       # 컬러 맵
            linewidths=5)        # 구분 선
plt.show()