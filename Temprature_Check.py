'''

Consider an array that contains temperature recorded in a city for every day for the month of January.
Thus the array will have 31 entries for 31 days of temperature.
Temperature values are integers between -50 to +50.
Return true if there was same temperature value for any two days in a month.

Example : 
Input : 
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

Output : False.


Input : 
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10,1, 12, 13, 14, 15, 16, 17, 18, 19, 20,1, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]



Output : True.

Pseudo Code:
Take the input list of numbers and range1,range2
index = range1
numbers = []
Iterate the loop with condition index <= range2
numbers.append(0)
index += 1
length = len(list)
index = 0
Iterate the loop for every element ‘ele’ of the list
numbers[ele-range1] += 1
Iterate the loop for every element ‘ele’ of the numbers
if(ele > 1)
return ‘true’
return false

'''
def Temprature_Check(list1,range1,range2):
    index = range1
    numbers = []
    while(index <= range2):
        numbers.append(0)
        index += 1
    length = len(list1)
    index = 0
    for ele in list1:
        numbers[ele-range1] += 1
    for ele in numbers:
        if(ele > 1):
            return 'true'
    return 'false'
print("The Temprature check for the given list of tempratures recorded in january month is:",Temprature_Check([1, 2, 3, 5, 5, 6, 7, 8, 9,10,11,12, 13, 14, 15, 16, 17, 18, 19, 20,21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],-50,50))

