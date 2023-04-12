import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')

sns.set_style('whitegrid')

# figure 서브 플롯 생성
fig = plt.figure(figsize=(15, 5))
ax1 = fig.add_subplot(1, 3, 1)
ax2 = fig.add_subplot(1, 3, 2)
ax3 = fig.add_subplot(1, 3, 3)

# x, y 변수 할당
sns.barplot(x='sex', y='survived', data=titanic, ax=ax1)
# x, y 변수 할당 + hue 옵션
sns.barplot(x='sex', y='survived', hue='class', data=titanic, ax=ax2)
# x, y 변수 할당 + hue 옵션 + dodge(누적 출력=false)
sns.barplot(x='sex', y='survived', hue='class', dodge=False, data=titanic, ax=ax3)

ax1.set_title('titanic survived - sex')
ax1.set_title('titanic survived - sex/class')
ax1.set_title('titanic survived - sex/class(stacked')

plt.show()