import pandas as pd
# install and execute panda library

df = pd.read_csv('/Users/alira/Desktop/Week 1/df.csv')

print(df)

df.info()  # get the information of this datafile
df.describe()
df.count()

print(df['Rating'])
print(df['Rating'][0])  # read index 0
print(df['Rating'][1])  # read index 1
print(df['Rating'][150])  # read index 150
print(int(df['Rating'][150]))   # read index 150 and convert it to int

print(df['Rating'].apply(int))
# df['column'].apply(function_name)
