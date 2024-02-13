import pandas as pd

df = pd.read_csv('/Users/alira/Desktop/Week 1/df.csv')
print(df)

print(df['Salary Estimate'][0])
print(df['Salary Estimate'][155])

text1 = df['Salary Estimate'][155]
print(text1)

text2 = text1.replace('$', '')  # replace $ sign with empty
print(text2)

text3 = 'I love data Science'
print(text3)
print(text3.replace('data Science', 'business'))

text4 = df['Salary Estimate'][12]
print(text4)
print(text4.replace('Glassdoor est.', 'Data Road Map.'))
