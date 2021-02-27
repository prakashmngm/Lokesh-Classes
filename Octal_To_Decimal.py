'''

Octal _To_Decimal:
 
Valid Inputs : 102 , 71, 3
Valid Outputs : 66, 57 , 3

Pseudo Code:
Take the input octal string
length = len(string)
str_index = length -1
exp_index = 0
sum = 0
Iterate the loop with condition str_index >= 0 or exp_index < length
sum += (string[str_index]*exponent(8,exp_index))
str_index -= 1
exp_index += 1
print(sum)

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

def Octal_To_Decimal(octal):
    length = len(octal)
    str_index = length-1
    exp_index = 0
    sum = 0
    while(str_index >= 0):
        sum += (int(octal[str_index])*exponent(8,exp_index))
        str_index -= 1
        exp_index += 1
    return sum

print(Octal_To_Decimal('100'))

