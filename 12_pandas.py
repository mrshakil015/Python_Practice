import numpy as np
import pandas as pd

student_dict = {
    "Name":['Shakil','Ridoy','Shaiful','Banna'],
    "ID":[15,11,14,13],
    "Address":['Hemayetpur','Kollanpur','Savar','Mirpur'],
}
students_tab = pd.DataFrame(student_dict)
print("Students List:\n",students_tab)
students_tab.to_csv('list.csv')
students_tab.to_csv('list_without_index.csv', index=False)
print("Show the first 2 rows:\n",students_tab.head(2))
print("Show the last 2 rows:\n",students_tab.tail(2))