'''
Problem : No of students passed based on marks list of the students.

marks = [ 99, 99, 99, 99, 99…..10lac  ]

Algorithm works for the second code than below one.

count = 0
for i in marks:
	if(i >= 35):
		count = count+1
print(“The number of students passed is:”,count)

Usually the number of students passed is very greater than number of students failed . Hence the below algorithm works very better than above code.

'''

marks = [22,20,39,43,23]

totalStudents = len(marks)
for i in marks:
	if( i < 35 ) :
	      totalStudents = totalStudents - 1
print("The number of students passed is:",totalStudents)


