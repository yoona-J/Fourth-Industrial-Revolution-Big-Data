import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

titanic = sns.load_dataset("titanic")

titanic['age'] = titanic['age'].fillna(titanic['age'].median())
titanic['embarked'] = titanic['embarked'].fillna('S')
titanic['embark_town'] = titanic['embark_town'].fillna('Southampton')
titanic['deck'] = titanic['deck'].fillna('C')

print(titanic['alone'].value_counts())

def category_age(x):
    if x < 10:
        return 0
    elif x < 20:
        return 1
    elif x < 30:
        return 2
    elif x < 40:
        return 3
    elif x < 50:
        return 4
    elif x < 60:
        return 5
    elif x < 70:
        return 6
    else:
        return 7

titanic['age2'] = titanic['age'].apply(category_age)
titanic['sex'] = titanic['sex'].map({'male': 1, 'female': 0})
titanic['family'] = titanic['sibsp'] + titanic['parch'] + 1

heatmap_data = titanic[['survived', 'sex', 'age2', 'family', 'pclass', 'fare']]
sns.heatmap(heatmap_data.astype(float).corr(), cmap='RdBu', annot = True)

plt.show()