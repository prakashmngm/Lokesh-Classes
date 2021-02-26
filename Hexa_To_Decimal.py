'''
Problem : 
Given a hexadecimal number, you to convert to decimal number.

Step1 : Come up with 3 valid inputs & respective outputs
Step2 : Pen-Paper solving of problem.
Step3 : Pseudocode. Dry run with Step1 inputs.
Step4 : Write code.

Valid inputs : F, E0, F20
Valid Outputs : 15, 224, 1312

Pseudo Code:
1.Take input Hexa-Decimal String(F20)
2.length = len(string)
3. str_index = length - 1
4. exp_index = 0
5. sum = 0
5. Iterate loop with condition str_index >= 0
	a. digit = string(str_index)
b. if(digit == ‘A’)
sum = sum +(10*exponent(16,exp_index))
c. elif(digit == ‘B’)
sum = sum +( 11*exponent(16,exp_index))
d.elif(digit == ‘C’)
sum = sum +(12*exponent(16,exp_index))
e.elif(digit == ‘D’)
sum = sum +(13*exponent(16,exp_index))
f. elif(digit == ‘E’)
sum = sum +(14*exponent(16,exp_index))
g.elif(digit == ‘F’)
sum = sum +(15*exponent(16,exp_index))
h.else
sum = sum +(digit*exponent(16,exp_index))
i. str_index = str_index - 1
j. exp_index = exp_index + 1
6.print sum

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

def Hexa_To_Decimal(string):
    length = len(string)
    str_index = length - 1
    exp_index = 0
    sum = 0
    while(str_index >= 0):
        digit = string[str_index]
        if(digit == 'A'):
            sum = sum +(10*exponent(16,exp_index))
        elif(digit == 'B'):
            sum = sum +( 11*exponent(16,exp_index))
        elif(digit == 'C'):
            sum = sum +(12*exponent(16,exp_index))
        elif(digit == 'D'):
            sum = sum +(13*exponent(16,exp_index))
        elif(digit == 'E'):
            sum = sum +(14*exponent(16,exp_index))
        elif(digit == 'F'):
            sum = sum +(15*exponent(16,exp_index))
        else:
            sum = sum +(int(digit)*exponent(16,exp_index))
        str_index = str_index - 1
        exp_index = exp_index + 1
    return sum

print(Hexa_To_Decimal('F'))

