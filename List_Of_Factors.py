'''

Given a number, find a list of all its divisors.
Input number > 1

Valid Inputs : 7,18,119
Valid output : [1,7],[1,2,3,6,9,18],[1,7,17]

Pseudo Code:
Take input number
divisor_list = [1]
divisor = 2
Iterate the loop with condition divisor <= num
if(num%divisor == 0)
Add divisor to the divisor_list
divisor += 1
print(divisor_list)

'''

def Divisor_List(num):
    divisor_list = [1]
    divisor = 2
    while(divisor <= num):
        if(num%divisor == 0):
            divisor_list.append(divisor)
        divisor += 1
    return divisor_list
    
print("The list of factors for the given number is:",Divisor_List(122))
            
    

