import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')

sns.set_style('whitegrid')

# figure 서브 플롯 생성
fig = plt.figure(figsize=(15, 5))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

# 이산형 변수 분포 - 데이터 분산 미고려
sns.stripplot(x="class",
              y="age",
              data=titanic,
              ax=ax1)

# 이산형 변수 분포 - 데이터 분산 고려
sns.swarmplot(x="class",
              y="age",
              data=titanic,
              ax=ax2)

ax1.set_title('Strip Plot1')
ax2.set_title('Strip Plot2')

plt.show()