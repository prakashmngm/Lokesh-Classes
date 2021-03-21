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
count = (range2-range1)+1
length = len(list)
numbers = []
index = 0
Iterate the loop with condition index < count
numbers.append(0)
index += 1
index = 0
Iterate the loop with condition index < length
ele = list[index]
index1 = 0
Iterate the loop with condition index1 < length 
if( ele < list[index1])
numbers[ele-range1] += 1
index1 += 1
               c. index += 1
10. Iterate the loop for every element ‘ele’ in the list
a. print(“The number of elements less than”+ele+”is:         “,numbers[ele-range1])


'''
def elements_less_than_each_element(list1,range1,range2):
    count = (range2-range1)+1
    length = len(list1)
    numbers = []
    index = 0
    while(index < count):
        numbers.append(0)
        index += 1
    index = 0
    while(index < length):
        ele = list1[index]
        index1 = 0
        while(index1 < length):
            if(ele > list1[index1]):
                numbers[ele-range1] += 1
            index1 += 1
        index += 1
    print(numbers)
    for ele in list1:
        print("The number of elements less than "+str(ele)+" is:",numbers[ele-range1])
print(elements_less_than_each_element([5, 6, 1, 1, 2, 3, 20],0,25))
