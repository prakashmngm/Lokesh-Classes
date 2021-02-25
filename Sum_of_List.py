'''
Problem : Summation of ‘n’ nos.

Consider a list of numbers. Print the sum of all the numbers.

Input : [ 1, 2, 3, 4, 5 ]
Output : 15


List down different “input cases” your program might get.
Eg - Empty List : []. Your program should return 0.
Single element List : [1].
List with +ve and -ve numbers.
List with integers as well as decimals.

Possible Inputs:

All possible inputs:
[],[1.2],[5,9],[4,7,9],[2,3,4,5],[6,7,8,9]

Pseudo Code:

1. Input the list of numbers
2. Initiate a variable called ‘sum’ to zero to store the sum of the elements of the list
3. iterate through each element of the list using for loop and add it to the sum.
4.print the value of the sum

'''

list = [ 1, 2, 3, 4, 5 ]
sum = 0
if(len(list)>1):
	for item in list:
		sum = sum+item
	print("The summation of elements of the given list is:",sum)
else:
	print("There has to be minimum two elements to perform sum of the list")

