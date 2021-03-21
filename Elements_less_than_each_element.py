'''
Consider an array with numbers.
0<= Numbers <= 25
For every number in the array, find how many numbers in the array are smaller than it.
Example : 
Input ->    [ 5, 6, 1, 1, 2, 3, 20]
Output->  [ 4, 5, 0, 0, 2, 3, 6 ]
Constraints : 
1)Sorting is NOT allowed.
2)Multiple passes over the input array NOT allowed.

Pseudo Code:
Take the input numbers list,range1,range2
length = len(list1)
numbers = []
index = range1
Iterate the loop with condition (index <= range2)
        numbers.append(0)
        index += 1
index = 0
Iterate the loop with condition(index < length)
    ele = list1[index]
    index1 = (ele-range1)+1
    Iterate the loop with condition(index1 < len(numbers))
            numbers[index1] += 1
            index1 += 1
        index += 1
smaller_list = []
Iterate the loop for every element ele in list1
        smaller_list.append(numbers[ele-range1])
return smaller_list

'''

def Elements_less_than_each_element(list1,range1,range2):
    length = len(list1)
    numbers = []
    index = range1
    while(index <= range2):
        numbers.append(0)
        index += 1
    index = 0
    while(index < length):
        ele = list1[index]
        index1 = (ele-range1)+1
        while(index1 < len(numbers)):
            numbers[index1] += 1
            index1 += 1
        index += 1
    smaller_list = []
    for ele in list1:
        smaller_list.append(numbers[ele-range1])
    return smaller_list
print("The list of smaller numbers of the each element of the given input list is :",Elements_less_than_each_element([5, 6, 1, 1, 2, 3, 20],0,25))

