import pandas as pd
import random

#cleaning up the data
df = pd.read_csv(r'/Users/kimnayun/Projects/Platform Management/Property_Rents_Test.csv',header=None)   # change the location to the local file
df[['ID','Rent','size','standard']] = df[0].str.split(";", expand = True)
df=df.drop(0,axis=1)
df['Rent per sqm'] = df['Rent'].astype(float)/df['size'].astype(float)
df = df.astype(float)
# print(df)

#identifying trend
df['GroupMean'] = df['Rent per sqm'].groupby(df['standard']).transform('mean')
df['GroupVariance'] = df['Rent per sqm'].groupby(df['standard']).transform('var')
df['GroupStdDev'] = df['Rent per sqm'].groupby(df['standard']).transform('std')

#Measuring the deviation of each data point
df['ZScore'] = (df['Rent per sqm']-df['GroupMean'])/df['GroupStdDev']   # this is working fine
print(df)

#Working with new data
#Code to generate random values for testing
df2 = pd.DataFrame(columns=['ID','Rent','size','standard','Rent per sqm'],index=range(1,101))
df2['ID'] = df2.reset_index().index
df2['Rent'] = df2.apply(lambda x: random.randrange(500,2500,25),axis=1)       #rent values from 500 to 2500 Euros at step of 25 Euros
df2['Rent per sqm'] = df2.apply(lambda x: round(random.uniform(10.0,30.0),2),axis=1)  # Rent per sqm , similar to the values from the sample data in class
df2['size'] = round(df2['Rent']/df2['Rent per sqm'], 2)
df2.to_csv('Test Data set 100 values.csv')
print(df2)