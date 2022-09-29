import pandas as pd

filepath = 'data/iris-write-from-docker.csv'

# read JSON file as dataframe
data = pd.read_csv(filepath)
print(data.iloc[:5])


# write dataframe file to JSON

data.to_jason('outputfile.json')




#import seaborn as sns
sns.set_context('paper')
### BEGIN SOLUTION
# This uses the `.plot.hist` method
ax = data.plot.hist(bins=25, alpha=0.5)
ax.set_xlabel('Size (cm)');



