import seaborn as sns
import pandas as pd

titanic = sns.load_dataset("titanic")

titanic['age'] = titanic['age'].fillna(titanic['age'].median())
titanic['embarked'] = titanic['embarked'].fillna('S')
titanic['embark_town'] = titanic['embark_town'].fillna('Southampton')
titanic['deck'] = titanic['deck'].fillna('C')

titanic_corr = titanic.corr(method='pearson')
titanic_corr.to_csv('C:/ch03_polls/titanic.csv', index = False)