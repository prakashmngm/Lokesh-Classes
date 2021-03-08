'''

Problem : 
Find the gcd of  given list of ‘N’ numbers.
Note : gcd(𝑎,𝑏,𝑐) = gcd(𝑎,(gcd(𝑏,𝑐))

Valid Inputs : (12,108,132),(108,292,1350,4096,1638,2644),(1060,1520,320)
Valid Outputs : 12 , 2 , 20

Pseudo Code:
Take input number list
length = len(list)
index = 1
gcd = list[0]
Iterate through the list with condition index < length
gcd = Euclidean_GCD(gcd,list[index])
index += 1
print(gcd)

'''
def Euclidean_GCD(num1,num2):
    while(num2 != 0):
        remainder = num1%num2
        num1 = num2
        num2 = remainder
    return num1

def GCD_Of_N_Numbers(list1):
    length = len(list1)
    index = 1
    gcd = list1[0]
    while(index < length):
        gcd = Euclidean_GCD(gcd,list1[index])
        index += 1
    return gcd
print("The gcd of given list of N Numbers is:",GCD_Of_N_Numbers([23,46,92]))

