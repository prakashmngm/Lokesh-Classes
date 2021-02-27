'''

Decimal _To_Octal:

Valid Inputs    :  8 , 72 , 100
Valid Outputs : 10 , 110 , 144

Pseudo Code:
Take the input num
octal = []
Iterate the loop with condition num >0
digit = num%8
octal.insert(0,digit)
num = num/8


'''

def Decimal_To_Octal(num):
    octal = []
    while(num > 0):
        octal.insert(0,str(num%8))
        num = num//8
    octa = ''.join(octal)
    return octa

print(Decimal_To_Octal(100))
