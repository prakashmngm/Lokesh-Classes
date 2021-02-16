'''
Sample Inputs : (1,2),(2,3),(3,3)

Sample Outputs : 1^0/0! + 1^1/1! + 1^2/2! = 1 + 1 + 1/2 = 2.5
		       2^0/0! + 2^1/1! + 2^2/2! + 2^3/3! = 1 + 2 + 2 + 8/6 =  6.333...
		       3^0/0! + 3^1/1! + 3^2/2! + 3^3/3! = 1 + 3 +  4.5 + 4.5 = 13
Pseudo Code
Take input variables base and num
index = 0
series = 0
Iterate index from 0 to given number with the condition index <= num
series += exponent(base,index) / factorial(index)
index += 1
Print the value of the variable series

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


def factorial(num):
    if(num == 0):
        return 1
    else:
        fact = 1
        index =1
        while(index <= num):
            fact *= index
            index = index+1
        return fact

base = 3
num = 3
index = 0
series = 0
while(index <= num):
    series += (exponent(base,index)/factorial(index))
    index += 1
print("The value of the Exponent - Factorial series is :",series)
