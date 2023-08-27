import pandas as pd

df = pd.read_csv('data.csv')

print(df)

print("shape of the dataframe: {shape}".format(shape=df.shape))
print("length of the dataframe: {length}".format(length=len(df)))
print("list of the dataframe columns: {columns}".format(columns=df.columns.tolist()))
print("length of the columns: {length}".format(length=len(df.columns)))
print("info of the dataframe:")
print(df.info())
print("head of the dataframe:")
print(df.head())
print("tail of the dataframe:")
print(df.tail())
print('range of rows between 5 to 9')
print(df[5:10])
print('print the top 3 row, default is 5')
print(df.head(3))
print('reverse the order of the dataframe')
print(df[::-1])
print('every 10th row b/w 1-100')
print(df[0:100:10])
# to fetch the 1 column then df['CountryName']
print('retrieve a few columns')
print(df[[
          'CountryName', 'CountryCode'
      ]])

print('descriptive statistics of the entire dataframe')
print(df.describe())

print('change the column names')
df.columns = ['Country_Name', 'Country_Code', 'BirthRate', 'InternetUsers', 'IncomeGroup']
print(df.head(1))

# add a column
print('add a column')
df['myCalc'] = df.BirthRate * df.InternetUsers
print(df.head(1))

# drop a column, axis = 0 means it's row
df = df.drop('myCalc', axis=1)
print(df.head(1))

# filter the data
print('Filter the data')
filter1 = df.InternetUsers < 2
filter2 = df.BirthRate > 40

print(df[filter1 & filter2])
