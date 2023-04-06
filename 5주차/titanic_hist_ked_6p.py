import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 가져오기
titanic = sns.load_dataset('titanic')
sns.set_style('darkgrid')

# 그래프 객체 생성
fig = plt.figure(figsize=(15, 5))
ax1 = fig.add_subplot(1, 3, 1)
ax2 = fig.add_subplot(1, 3, 2)
ax3 = fig.add_subplot(1, 3, 3)

# hist + ked
sns.distplot(titanic['fare'], ax=ax1)
# no hist (histogram)
sns.distplot(titanic['fare'], hist=False, ax=ax2)
# no ked (kernel density)
sns.distplot(titanic['fare'], kde=False, ax=ax3)

ax1.set_title('titanic fare - hist/ked')
ax2.set_title('titanic fare - ked')
ax3.set_title('titanic fare - hist')

plt.show()
