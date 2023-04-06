import seaborn as sns

titanic = sns.load_dataset('titanic')

print(titanic.head(10))
print('----------------')
print(titanic.info())