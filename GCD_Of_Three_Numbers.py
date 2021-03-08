'''
Problem:
Given three numbers, find their gcd using Divisor-List.
Note : gcd(𝑎,𝑏,𝑐) = gcd(𝑎,(gcd(𝑏,𝑐))𝑏,𝑐))

'''

def Divisor_List(num):
    divisor = 1
    divisor_list = []
    sq_root = num**0.5
    while(divisor <= sq_root):
        if(num%divisor == 0):
            divisor_list.append(divisor)
            pair_divisor = num//divisor
            if(pair_divisor != divisor):
                divisor_list.append(pair_divisor)
        divisor += 1
    return divisor_list

def GCD_Of_Three_Numbers(num1,num2,num3):
    num1_list = sorted(Divisor_List(num1),reverse=True)
    num2_list = Divisor_List(num2)
    num3_list = Divisor_List(num3)
    for ele1 in num1_list:
        for ele2 in num2_list:
            flag = 0
            if(ele1 == ele2):
                flag = 1
                gcd = ele1
                break
        if(flag == 1):
            break
    print("GCD of num1 and num2 is:",gcd)
    gcd_list = sorted(Divisor_List(gcd),reverse=True)
    for ele3 in gcd_list:
        for ele4 in num3_list:
            if(ele3 == ele4):
                return ele3
     
print("The GCD Of num1 , num2 and num3 is:",GCD_Of_Three_Numbers(12,108,132))


