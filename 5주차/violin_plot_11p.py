import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')

sns.set_style('whitegrid')

# figure 서브 플롯 생성
fig = plt.figure(figsize=(15, 5))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

sns.boxplot(x='alive', y='age', data=titanic, ax=ax1)
sns.violinplot(x='alive', y='age', data=titanic, ax=ax2)

plt.show