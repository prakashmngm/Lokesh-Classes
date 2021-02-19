'''
Problem : Digits to Number Conversion.
Minimum no. of digits = 1
Max no. of digits : 50


Input : [ 2, 3, 7, 9 ]
Output : 2379

Input : [5]
Output : 5

Input : [2,5]
Output : 25

Pseudo Code:

Take the input list of digits
Calculate the length of list and store it in the variable ‘len’
Initiate a variable num = 0
Initiate a index variable = 1
Iterate index from 1 to len with condition index <= len
num += list[0]*exponent(10,len-index)
index += 1
Print the value of num


'''
def exponent(base,index):
    if(index == 0 and base == 0):
        return -1
    elif(index == 0):
        return 1
    elif(base == 0):
        return 0
    else:
        product = 1
        for indices in range(index):
            product *= base
        return product


list1 = [1,0,0,0,0,0,1]
length = len(list1)
num = 0
index = 1
while(index <= length):
    '''if(list1[index-1] == 0):
        #num += 0
    else:
    '''
    num += (list1[index-1]*exponent(10,length-index))
    index += 1
print("The value of num from the given digits is :",num)




