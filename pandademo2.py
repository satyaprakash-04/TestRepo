import pandas as pd

whether_info = {
    'day': ['11-09-2022', '12-09-2022', '13-09-2022', '14-09-2022', '15-09-2022'],
    'temperature': [33, 34, 32, 36, 37],
    'wind_speed': [12, 15, 16, 18, 19],
    'events': ['rain', 'sunny', 'snow', 'sunny', 'cloudy']

}

df = pd.DataFrame(whether_info)

# To print Data.
print(df)

# To print rows And columns
# rows, columns = df.shape
# print("rows: ", rows)
# print("columns: ", columns)
#
# # To print initial first rows
#
# print('initial first rows\n', df.head())
#
# print('Last few rows\n', df.tail())
#
# # Specified Rows
# print('first two rows\n', df.head(2))
# print('Last two rows\n', df.tail(2))
#
#
# # Slicing in Pandas
#
# # To print specified number of rows
#
# print('from 2nd to 4th row\n', df[2:4])
# print('All rows\n', df[:])
# print('print  rows with steps\n', df[1:5:2])
#
# # to print all columns.
# print('all columns\n', df.columns)
#
# # to print specified columns
#
# print("to print specified column", df.events)
# ''' here 'events' is the column name'''
#
# # to know the types of data
#
# print('type of data: ', type(df['day']))
# ''' basically the type of columns in pandas are series'''
#
# # To print specified columns
#
# print('print events and day\n', df[['events', 'day']])

# To get the particular Row

print('the index \'2\' row:\n', df.loc[2])

print('to print the temperature column: ', df['temperature'])

# To print the maximum temperature

print('the maximum temperature is: ', df['temperature'].max())

# to print the minimum temperature.

print('the minimum temperature is: ', df['temperature'].min())

# To print the average temperature

print('The average Temperature is: ', df['temperature'].mean())

# To get the description of the dataset

print('The description of the dataset is: \n', df.describe())

# To get temperature greater and  equals 34

print('the temperature >= 32 is: \n', df[df.temperature >= 34])

#  if the column contains spaces then use

# print('The temperature is: ', df[df.temperature == df['temperature'] >= 33])

#  By default pandas set the index from 0-x
# to see the index use
print('the index vvalue is: ', df.index)
#  To Change the index to the specified field.

print('the specified field index is: \n', df.set_index('day'))
# The above operation returns the new dataframe but does not modify it.
# To change the dataframe and get the modification result

print('To modify the dataframe for the index is: ', df.set_index('day', inplace=True))
#  NOw print dataframe and the location of the dataframe.
print('The dataframe: \n', df)
print('the specified row is by using the index is :\n', df.loc['12-09-2022'])

# To reset the index to the original one use

df.reset_index(inplace=True)
#  Now print Dataframe
print(df)

# Whenever setting the index if column contains the duplicate value the it adds the default index
# followed by the set index.
# New line Added.






