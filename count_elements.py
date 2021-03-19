'''

Problem : 
Consider an array consisting of students' marks for a subject.
0 <= Marks <= 50
Count the number of students for each mark from 0 to 50.

Input : [2, 5, 17, 21, 35, 2, 21, 5, 16, 2, 19]
Output : 
Marks0 : 0
Marks1 : 0
Marks2 : 3
Marks3 : 0
Marks4 : 0
Marks5 : 2
.
.
.
Marks50 : 0

Pseudo Code:
Take the input list of numbers
marks = []
index = 0
Iterate from 0 to count and append 0's to marks with condition index <= count
Iterate through given input list and increment corresponding marks in each iteration
print marks

'''

def Count_Elements(list1,count):
    marks = []
    index = 0
    while(index <= count):
        marks.append(0)
        index += 1
    for ele in list1:
        marks[ele] += 1
    print(marks)
    index = 0
    while(index < len(marks)):
        print('marks('+str(index)+') :',marks[index])
        index += 1
        
print(Count_Elements([2, 5, 17, 21, 35, 2, 21, 5, 16, 2, 19],50))


