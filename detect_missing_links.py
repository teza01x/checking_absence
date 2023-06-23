import pandas as pd


donor_table = 'your_name.xlsx'

second_table = 'your_name.xlsx'

df1 = pd.read_excel(donor_table)
link_column1 = df1['Supplier Product Link']

one_list = list()
second_list = list()

for i in range(len(link_column1)):
    one_list.append(link_column1.iloc[i])

df2 = pd.read_excel(second_table)
link_column2 = df2['LINK']

for i in range(len(link_column2)):
    second_list.append(link_column2.iloc[i])

for i in one_list:
    if i in second_list:
        pass
    else:
        print(i)