'''

Problem : Given an array of ‘n’ numbers, rearrange the numbers, so that they appear reverse.


Valid Inputs : [2,3,5,8,9],[1,7,11,15],[1,3,7,9]
                                                        
Valid Outputs : [9,8,5,3,2],[15,11,7,1]

Pseudo Code:
Take the input list
start_index = 0
end_index = len(list)-1
Iterate the loop with condition start_index < end_index
temp = list[start_index]
list[start_index] = list[end_index]
list[end_index] = temp
start_index += 1
end_index -= 1
print(list)


'''
def Reversing_Of_List(list1):
    start_index = 0
    end_index = len(list1)-1
    while(start_index < end_index):
        temp = list1[start_index]
        list1[start_index] = list1[end_index]
        list1[end_index] = temp
        start_index += 1
        end_index -= 1
    return list1

print("The reverse of given list is:",Reversing_Of_List([1,2,3,6,0,12]))
