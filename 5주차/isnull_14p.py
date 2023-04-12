import seaborn as sns

titanic = sns.load_dataset('titanic')
print(titanic.isnull().sum())

titanic['age'] = titanic['age'].fillna(titanic['age'].median())

# embarked에 어떤 값이 있는지 확인 후 null 값을 'S'로 치환
# value_counts -> 해당 값과 계수를 리턴
print(titanic['embarked'].value_counts())
titanic['embarked'] = titanic['embarked'].fillna('S')

# embarked_town에 어떤 값이 있는지 확인 후 null 값을 'Southampton'로 치환
print(titanic['embarked_town'].value_counts())
titanic['embarked_town'] = titanic['embarked_town'].fillna('Southampton')

# deck에 어떤 값이 있는지 확인 후 null 값을 'C'로 치환
print(titanic['deck'].value_counts())
titanic['deck'] = titanic['deck'].fillna('C')

print(titanic.isnull().sum())