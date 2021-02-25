'''

Problem : Find the factorial. Input will be integers >= 0

Input : 5
Output : 120


List of Valid Input : 
0,20,12,7,11

Pseudo Code : 
Take the input as the number to which factorial needs to be computed
If number is equal to 0 , print the factorial of the number is 1
Else got to step 4
Factorial = 1
Let index = 1
Iterate from variable index to given number and in each iteration 
a)multiply the variable  index with variable Factorial
b) store the result in variable factorial 
c) increment the index by 1


Print the factorial of the given number atleast

'''

def Factorial(num):
    if(num == 0):
        return 1
    else:
        fact = 1
        index =1
        while(index <= num):
            fact *= index
            index = index+1
        '''
        fact = 1    
        for index in range(1,num+1):
            fact *= index
        '''
        return fact

print(Factorial(0))
print(Factorial(5))

