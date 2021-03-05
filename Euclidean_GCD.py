'''

Find gcd of two numbers using Euclid’s Algorithm

Valid Inputs : (6,9),(12,16),(270,192)
Valid Outputs : 3 , 4 , 6

Pseudo Code:
Take the input number num1,num2
while(num2 != 0)
remainder = num1%num2
num1 = num2
num2 = remainder
print(num1)

'''

def Euclidean_GCD(num1,num2):
    while(num2 != 0):
        remainder = num1%num2
        num1 = num2
        num2 = remainder
        print("num1 and num2 :",num1,num2)
    return num1
print("The Euclidean GCD of the given two numbers is:",Euclidean_GCD(1024,4096))
        

