import numpy as np
import pandas as pd

student_dict = {
    "Name":['Shakil','Ridoy','Shaiful','Banna'],
    "ID":[15,11,14,13],
    "Address":['Hemayetpur','Kollanpur','Savar','Mirpur'],
    "Age":[23,24,26,25]
}
students_tab = pd.DataFrame(student_dict)
print("Students List:\n",students_tab)
students_tab.to_csv('list.csv')
students_tab.to_csv('list_without_index.csv', index=False)
print("Show the first 2 rows:\n",students_tab.head(2))
print("Show the last 2 rows:\n",students_tab.tail(2))
print("\nDescribe the data frame:\n",students_tab.describe())
studentList2 = pd.read_csv('StudentList.csv')
print("\nStudents List 2:\n",studentList2)
print("Print the student list 2 Marks:\n",studentList2['Roll NO'])
print("Print 1 index student roll:",studentList2['Roll NO'][1])