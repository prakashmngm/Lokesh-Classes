'''
Consider an array of ‘n’ numbers.
Consider an input index ‘k’.
Move the number at ‘k’ th position to the first position in array.
Move the number at (k+1)th position to the second position in array.
Move the number at (k+2)th position to the third position in array.


Example : 
[ 45, 5, 11, 33, 66, 44, 77, 8, 9 ]
Let k = 3

So 11 will go to first position.
And 33 will go to second position….and so on
Basically all numbers will left-shift by two positions.

Output : 
[11, 33, 66, 44, 77, 8, 9, 45, 5]  

Pseudo Code:
Take the input list and index ‘k’
length = len(list)
index = 0
k_index = k-1
Take the backup_list for the elements upto k_index
Iterate the loop with condition k_index <= length-1
list1[index] = list1[k_index]
index += 1
k-index += 1
Attach the backup_list to the list starting from k-1 from the end of the list
Print list

'''

def Left_Shift(list1,k):
    length = len(list1)
    index = 0
    k_index = k-1
    backup_list = []
    while(index < k_index):
        backup_list.append(list1[index])
        index += 1
    print(backup_list)
    index = 0
    while(k_index <= length-1):
        list1[index] = list1[k_index]
        index += 1
        k_index += 1
    print(list1)
    k_index = -(k-1)
    for ele in backup_list:
        list1[k_index] = ele
        k_index += 1
    return list1
    
print("The left shift of the given list is:",Left_Shift([45, 5, 11, 33, 66, 44, 77, 8, 9],9))


