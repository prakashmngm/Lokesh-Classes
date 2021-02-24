'''
Given an input number in the decimal system, convert it into binary.

Input : 8
Output : 1000

Input : 25
Output : 11001


Take the input number ‘num’
If num = 0 then return 0 else go to step 3
Binary = “”
Iterate loop with condition num>0
digit = num%2
Preappend digit to Binary
num = num/2
Print Binary

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
print("The binary number of num is:",Decimal_To_Binary(9))    

        
            

