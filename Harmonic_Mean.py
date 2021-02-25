'''
Problem : Harmonic Mean of ‘N’ numbers.


Pseudo code:

1. Input the list of numbers
2. Initiate a variable called ‘sum’ to zero to store the sum of the elements of the list
3.iterate through each element of the list using for loop and  reciprocate the item and add it to the sum
4.calculate the Harmonic Mean by reciprocating the sum which is calculated by the reciprocals of the items of the list
5.print the value of the Harmonic Mean

'''

list = [1,2,4]
sum = 0
length = len(list)
if(length>1):
	for item in list:
		sum += (1/item)
	HM = length/sum
	print("The Harmonic Mean of the elements in the list:",HM)
else:
	print("There has to be minimum 2 elements to perform the sum of the list")

