'''
Problem : 
Consider an array with numbers.
0<= Numbers <= 100
Count how many numbers appear in the array only once.

Input : [ 2, 3, 5, 2, 4, 2, 6, 4, 3, 2]
Output : 2

Pseudo Code:
Take the input list containing numbers from range-0 to range-100 and count = 100
numbers = []
index = 0
count = (range2-range1)+1
Iterate the loop from 0 to 100 with condition index < count
numbers.append(0)
index += 1
Iterate through every element 'ele' in list
numbers[ele-range1] += 1
total = 0
Iterate through every element 'ele' in numbers
if(ele == 1):
total += 1
print(total)
'''
def Unique_Elements(list1,range1,range2):
    numbers = []
    index = 0
    count = (range2-range1)+1
    while(index < count):
        numbers.append(0)
        index += 1
    for ele in list1:
        numbers[ele-range1] += 1
    total = 0
    for ele in numbers:
        if(ele == 1):
            total += 1
    return total

print(Unique_Elements([9,12,17,16,19,22,50,33,48,37,44,49],0,100))
    
