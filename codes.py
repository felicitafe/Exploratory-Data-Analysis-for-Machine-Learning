import pandas as pd

filepath = 'data/iris-write-from-docker.csv'
data = pd.read_csv(filepath)
print(data.iloc[:5])

