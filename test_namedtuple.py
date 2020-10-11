'''
INPUT
1. Columns can be in any order. IDs, marks, class and name can be written in any order in the spreadsheet.
2. Column names are ID, MARKS, CLASS and NAME. (The spelling and case type of these names won't change.)

The first line contains an integer N, the total number of students.
The second line contains the names of the columns in any order.
The next N lines contains the marks, IDs, name and class , under their respective column names.

e.g.,
5
ID         MARKS      NAME       CLASS
1          97         Raymond    7
2          50         Steven     4
3          91         Adrian     9
4          72         Stewart    5
5          80         Peter      6

Output Format

Print the average marks of the list corrected to 2 decimal places.
'''


from collections import namedtuple
n=int(input())
fields=input().split()
#print(fields)
student=namedtuple('Student',fields)
#records=[]
marks=0
for i in range(n):
    field1,field2,field3,field4 = input().split()
    #records.append(student(field1,field2,field3,field4))
    st=student(field1,field2,field3,field4)
    marks += int(st.MARKS)
print(f'{marks/n:.2f}')
