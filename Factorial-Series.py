'''

Consider the series : = 0! + 1! + 2! + 3! =  1 + 1 + 2 + 6 = 10 

Input : 3
Output : 10

Input : 5
Output : 154 
(0! + 1! + 2! + 3! + 4! + 5! )


Use the def Factorial(num): function that we have written before.

'''

def Factorial(num):
    if(num == 0):
        return 1
    else:
        fact = 1
        index =1
        while(index <= num):
            fact *= index
            index = index+1
        return fact
  
num = 5
series = 0
index = 0
while(index <= num):
	series += Factorial(index)
	#print(num,series,index)
	index = index+1
print("The value of Factorial series is :",series)

