import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 가져오기
titanic = sns.load_dataset('titanic')
sns.set_style('darkgrid')

# 그래프 객체 생성
fig = plt.figure(figsize=(15, 5))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

# 그래프 그리기
# fit_reg => 회귀선 표시 여부
sns.regplot(x='age', y='fare', data=titanic, ax=ax1, fit_reg=True)
sns.regplot(x='age', y='fare', data=titanic, ax=ax2, fit_reg=False)

plt.show()
