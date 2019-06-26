import pandas as pd

filepath='E:\sample1\ptestdata.xlsx'

xl=pd.read_excel(filepath,sheet_name='Sheet1')

'''print(xl)

column=xl['username']
print(column)

column1=xl[['username','password']]
print(column1)

row=xl[0:1]
print(row)

row1=xl[0:2]
print(row1)

head=(xl.head())
print(head)

head1=(xl.head(3))
print(head1)

tail=(xl.tail())
print(tail)

tail1=(xl.tail(2))
print(tail1)

size=xl.shape
print(size)
print('the row count is',size[0])
print('the column count is',size[1])'''

'''row1=xl.iloc[0]
print(row1)

row2=xl.iloc[1]
print(row2)

row3=xl.iloc[-1]
print(row3)

row4=xl.iloc[[2,3,4]]
print(row4)

row5=xl.iloc[1:4]
print(row5)'''

'''col=xl.iloc[:,0]
print(col)

col1=xl.iloc[:,-1]
print(col1)

col2=xl.iloc[:,0:3]
print(col2)

col3=xl.iloc[:,[2,3]]
print(col3)

col4=xl.iloc[0:1,0:3]
print(col4)'''

row_value=xl.loc[0]
print(row_value)


