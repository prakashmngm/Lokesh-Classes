'''

Given input Hexadecimal number, convert it into Binary.

Valid Inputs    :  D , 3B , 2AE
Valid Outputs : 1101 , 111011 , 1010101110

Pseudo Code:
Take the input Hexadecimal string
num = Hexa_To_Decimal(string)
binary = Decimal_To_Binary(num)
Print the output binary string

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
    
def Decimal_To_Binary(num):
    if(num == 0):
        return 0
    else:
        binary = []
        while(num > 0):
            binary.insert(0,str(num%2))
            num = num//2
        binary_string = ''.join(binary)
        return binary_string

def Hexa_To_Binary(string):
    num = Hexa_To_Decimal(string)
    binary = Decimal_To_Binary(num)
    return binary
print(Hexa_To_Binary('D'))

