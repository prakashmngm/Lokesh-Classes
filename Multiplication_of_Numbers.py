'''

Problem : Multiplication of two positive integers.
Function : def multiplication(num1, num2)

Using addition.


Input : multiplication( 5, 7)
Output : 35



PseudoCode :
Input : (5,5),(5,0.7),(0.4,0.3),(-5,0.3),(-7,-8),(-0.2,-0.9)

1.take two input integers num1,num2
2.initiate a sum variable to 0
3.If num1 and num2 is not equal to 0 .go to step 4 else got to step 6
4.if num1>=num2 , iterate num2, num1 number of times and add it to sum variable in each iteration.
5.if num2>num1 , iterate num1 , num2 number of times and add it to sum variable in each iteration.
6. Print the value of the sum variable as final multiplication value.


'''

def multiplication(num1,num2):
    sum = 0
    if((num1 and num2) != 0):
        if(num1>num2):
            for index in range(num2):
                sum += num1
        else:
            for index in range(num1):
                sum += num2
    print("The product of the integers is:",sum)
    
multiplication(5,6)


