'''

Problem : Given a number, find its smallest divisor > 1.
Integer > 0


Step1) List of 3 valid inputs & 3 valid outputs
Step2) Pen & Paper algorithm
Step3) Pseudocode + Dry run
Step4) Coding

Step 1) 4, 19 , 111

Step 2)  2 , 19 , 3



Pseudo Code:

Take the input number : num
if(num%2 == 0)
return 2
elif(num%3 == 0)
return 3
else
divisor = 5
Iterate the loop with condition divisor <= num
if(num%divisor == 0)
return divisor
else
divisor = divisor +2


'''
def smallest_factor(num):
    if(num%2 == 0):
        return 2
    elif(num%3 == 0):
        return 3
    else:
        divisor = 5
        while(divisor <= num):
            if(num%divisor == 0):
                return divisor
            else:
                divisor += 2
print("The smallest of the given number is :",smallest_factor(121))

