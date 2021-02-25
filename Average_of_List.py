'''
Problem : Average of all the elements of a List.


Pseudo Code:

1. Input the list of numbers
2. Initiate a variable called ‘sum’ to zero to store the sum of the elements of the list
3.iterate through each element of the list using for loop and add it to the sum.
4.calculate the average by dividing the sum with length of the list.
5.print the value of the average


'''

list = [ 1, 2, 3, 4, 6 ]
sum = 0
length = len(list)
if(length > 1):
	for item in list:
		sum = sum+item
	avg = sum/length
	print("The average of elements in the list :",avg)
else:
	print("There has to be minimum 2 elements to perform the sum of the list")



