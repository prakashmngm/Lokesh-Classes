'''
Given two numbers, find their GCD

Valid Inputs : (6,9),(12,18),(121,132)
Valid Outputs : 3 , 6 , 11

Pseudo Code:

Take the input numbers num1,num2
num1_list = sorted(Divisor_List(num1),reverse = True)
num2_list = Divisor_List(num2)
Iterate loop for the elements in num1_list
Iterate loop for the elements in num2_list
if(ele_num1 == ele_num2)
print(“GCD is :”,ele_num1

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

def GCD_Of_Two_Numbers(num1,num2):
    num1_list = sorted(Divisor_List(num1),reverse=True)
    num2_list = Divisor_List(num2)
    for ele_num1 in num1_list:
        for ele_num2 in num2_list:
            if(ele_num1 == ele_num2):
                return ele_num1
print("The GCD Of Given Two Numbers is:",GCD_Of_Two_Numbers(1060,1520))
    

