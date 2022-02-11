import pandas as pd

filepath = 'data/iris-write-from-docker.csv'

# read JSON file as dataframe
data = pd.read_csv(filepath)
print(data.iloc[:5])


# write dataframe file to JSON

data.to_jason('outputfile.json')



