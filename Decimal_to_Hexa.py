'''
Problem : Given an input decimal number, convert it into hexadecimal format.

Input : 5
Output : 5

Input : 17
Output : 11

Input : 62
Output : 3E

Pseudo Code:

1.Take the input number ‘num’
2.if num = 0 return 1 else goto step3
3.list = []
4.Iterate loop with condition num >0
	a. digit = num%16
	b. if(digit >9)
		if(digit = 10)
			list.insert(0,A)
		elif(digit = 11)
			list.insert(0,B)
		elif(digit = 12)
			list.insert(0,C)
		elif(digit = 13)
			list.insert(0,D)
		elif(digit = 14)
			list.insert(0,E)
		else(digit = 15)
			list.insert(0.F)
	c. else
	    list.insert(0,digit)
	d. num = num/16
5.return list after converting it into string

'''
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
print("The Hexadecimal number of num is:",Decimal_To_Hexadecimal(3298)) 

