import numpy as np
import pandas as pd


#_______________________________T-A-S-K-1___________________________________


# data = {
#     'Name': ['Alex', 'Bella', 'Chris'],
#     'Age': [30, 25, 35],
#     'City': ['Kyiv', 'Lviv', 'Odesa']
# }
# df1 = pd.DataFrame(data)
# df1['Salary'] = [50000, 60000, 55000]

# df1 = df1.drop(columns=['Age'])

# new_row1 = pd.DataFrame([{'Name': 'Diana', 'City': 'Dnipro', 'Salary': 58000}])
# df1 = pd.concat([df1, new_row1], ignore_index=True)

# df1 = df1.drop(index=0).reset_index(drop=True)

# df1['Department'] = 'Sales'

# df1 = df1.drop(columns=['Salary'])

# print("Завдання 1:\n", df1)



#_______________________________T-A-S-K-2___________________________________



# data = {
#     'Product': ['Book', 'Pen', 'Notebook'],
#     'Price': [15, 2, 5],
#     'Stock': [100, 500, 200]
# }
# df2 = pd.DataFrame(data)


# df2['Discount'] = '10%'
# df2 = df2.drop(columns=['Stock'])

# new_row2 = pd.DataFrame([{'Product': 'Pencil', 'Price': 1, 'Discount': '5%'}])
# df2 = pd.concat([df2, new_row2], ignore_index=True)

# df2 = df2.drop(index=1).reset_index(drop=True)

# df2['Supplier'] = 'Stationery Co.'

# df2 = df2.drop(index=2).reset_index(drop=True)

# print("\nЗавдання 2:\n", df2)



#_______________________________T-A-S-K-3___________________________________



# data = {
#     'Employee': ['John', 'Emma', 'Oliver'],
#     'Department': ['HR', 'Finance', 'IT'],
#     'Salary': [50000, 70000, 60000],
#     'Age': [28, 34, 29]
# }
# df3 = pd.DataFrame(data)

# df3['Bonus'] = df3['Salary'] * 0.10

# df3 = df3.drop(columns=['Age'])

# new_row3 = pd.DataFrame([{'Employee': 'Sophia', 'Department': 'Marketing', 'Salary': 65000, 'Bonus': 6500}])
# df3 = pd.concat([df3, new_row3], ignore_index=True)

# df3 = df3.drop(index=0).reset_index(drop=True)

# df3 = df3.drop(columns=['Bonus'])
# print("\nЗавдання 3:\n", df3)