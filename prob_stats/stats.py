import pandas as pd
from scipy import stats

# import and parse data
data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''

data = data.splitlines()
data = [i.split(', ') for i in data]

# put data in a dataframe
cols = data[0]
rows = data[1::]
df = pd.DataFrame(rows, columns=cols)

# convert number values to float
df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

# print mean, median, and mode values
print('The mean, median, and mode values for the Alcohol and Tobacco spending dataset are as follows:')
print 'The mean spending on Alcohol is ' + str(df['Alcohol'].mean())
print 'The mean spending on Tobacco is ' + str(df['Tobacco'].mean())
print 'The median spending on Alcohol is ' + str(df['Alcohol'].median())
print 'The median spending on Tobacco is ' + str(df['Tobacco'].median())
print 'The mode spending on Alcohol is ' + str(stats.mode(df['Alcohol'])[0][0])
print 'The mode spending on Tobacco is ' + str(stats.mode(df['Tobacco'])[0][0])
