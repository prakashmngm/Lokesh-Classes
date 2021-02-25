'''

Given a binary number, you to convert into decimal number.

Valid inputs : 10010 ,0110,1001110,1
Valid Outputs : 18,6,78


Valid Input : 0, 1,  10,11,00,01,110

Valid Output : 0, 1,2,3,6 

Pseudo Code:
	1. Take the input Binary string 
	2. length = len(string)
	3. sum = 0 
	4. str_index = len-1
	5. exp_index = 0
	5.Iterate loop with condition str_index >= 0 or exp_index < length
		a.  sum = sum + (str[str_index]*exp(2,exp_index))
        b.  str_index = str_index-1
		c.  exp_index = exp_index+1
	6. print sum


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
        
def Binary_to_Decimal(string):
    length = len(string)
    sum = 0
    str_index = length - 1
    exp_index = 0
    while(str_index >= 0):
        sum = sum + (int(string[str_index])*exponent(2,exp_index))
        str_index = str_index-1
        exp_index = exp_index+1
    return sum
    
print("The decimal number to the given binary number is :",Binary_to_Decimal('11'))
    

