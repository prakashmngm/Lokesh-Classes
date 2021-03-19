'''
Problem : 
Consider an array with numbers.
0<= Numbers <= 100
Count how many numbers appear in the array only once.

Input : [ 2, 3, 5, 2, 4, 2, 6, 4, 3, 2]
Output : 2

Pseudo Code:
Take the input list containing numbers from 0 to 100 and count = 100
numbers = []
index = 0
Iterate the loop from 0 to 100 with condition index <= count
numbers.append(0)
index += 1
Iterate through every element 'ele' in list
numbers[ele] += 1
total = 0
Iterate through every element 'ele' in numbers
if(ele == 1):
total += 1
print(total)
'''
def Unique_Elements(list1,count):
    numbers = []
    index = 0
    while(index <= count):
        numbers.append(0)
        index += 1
    for ele in list1:
        numbers[ele] += 1
    total = 0
    for ele in numbers:
        if(ele == 1):
            total += 1
    return total

print(Unique_Elements([2, 3, 4, 2, 4, 2, 6, 3, 98, 2],100))
    
