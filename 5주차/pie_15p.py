import seaborn as sns

titanic = sns.load_dataset('titanic')
print(titanic.isnull().sum())

titanic['age'] = titanic['age'].fillna(titanic['age'].median())

# embarked에 어떤 값이 있는지 확인 후 null 값을 'S'로 치환
# value_counts -> 해당 값과 계수를 리턴
print(titanic['embarked'].value_counts())
titanic['embarked'] = titanic['embarked'].fillna('S')

# embark_town에 어떤 값이 있는지 확인 후 null 값을 'Southampton'로 치환
print(titanic['embark_town'].value_counts())
titanic['embark_town'] = titanic['embark_town'].fillna('Southampton')

# deck에 어떤 값이 있는지 확인 후 null 값을 'C'로 치환
print(titanic['deck'].value_counts())
titanic['deck'] = titanic['deck'].fillna('C')

print(titanic.isnull().sum())

# pie flot

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 5))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

# 남성 생존자 값을 pie 그래프로
m_sur = titanic['survived'][titanic['sex'] == 'male'].value_counts()
print(m_sur)
m_sur.plot(kind='pie', explode=[0, 0.1], autopct='%1.1f%%', ax=ax1, shadow=True)

# 여성 생존자 값을 pie 그래프로
f_sur = titanic['survived'][titanic['sex'] == 'female'].value_counts()
print(f_sur)
f_sur.plot(kind='pie', explode=[0, 0.1], autopct='%1.1f%%', ax=ax2, shadow=True)

ax1.set_title('Survived (Male)')
ax2.set_title('Survived (Female)')

plt.show()