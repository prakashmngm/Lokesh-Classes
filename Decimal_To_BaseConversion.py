'''
def DecimalToBaseConversion( Integer num, Integer base ) : 

Num : Integer>=0
Base : 2, 8, 16

Pseudo Code:
Take the input num , base
if(base == 2)
binary = Decimal_To_Binary(num)
print(binary)
elif(base == 8)
octal = Decimal_To_Octal(num)
print(octal)
elif(base == 16)
hexa = Decimal_To_Hexa(num)
print(hexa)
else
print(“Please enter the correct base to convert the given decimal number”)

'''
def Decimal_To_Binary(num):
    if(num == 0):
        return 0
    else:
        binary = []
        while(num > 0):
            binary.insert(0,str(num%2))
            num = num//2
            print(num)
        binary_string = ''.join(binary)
        return binary_string

def Decimal_To_Hexadecimal(num):
    if(num == 0):
        return 0
    else:
        hexa = []
        while(num > 0):
            digit = num%16
            if(digit > 9):
                if(digit == 10):
                    hexa.insert(0,'A')
                elif(digit == 11):
                    hexa.insert(0,'B')
                elif(digit == 12):
                    hexa.insert(0,'C')
                elif(digit == 13):
                    hexa.insert(0,'D')
                elif(digit == 14):
                    hexa.insert(0,'E')
                else:
                    hexa.insert(0,'F')
            else:
                hexa.insert(0,str(digit))
            num = num//16
        hexa_string = ''.join(hexa)
        return hexa_string

def Decimal_To_Octal(num):
    octal = []
    while(num > 0):
        octal.insert(0,str(num%8))
        num = num//8
    octa = ''.join(octal)
    return octa

def Decimal_To_BaseConversion(num,base):
    if(base == 2):
        binary = Decimal_To_Binary(num)
        return binary
    elif(base == 8):
        octal = Decimal_To_Octal(num)
        return octal
    elif(base == 16):
        hexa = Decimal_To_Hexadecimal(num)
        return hexa
    else:
        print("Please enter the correct base to convert the given decimal number")
print(DecimalToBaseConversion(12,16))
    
