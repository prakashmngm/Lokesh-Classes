'''
Problem : Modify Summation of elements of the list such that for ‘n’ input numbers, there are (n-1) additions.

'''

list = [5,2,3,8,9]
length = len(list)
if(length > 0):
    sum = list[0]
    index = 1
    while(index < length):
        sum += list[index]
        index += 1
    print("The sum of the elements of the list :",sum)
else:
    print("There has to be minimum one element in the list to perform addition")
