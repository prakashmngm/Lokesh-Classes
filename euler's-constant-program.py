'''
Sample Inputs : 0,5,4
Pseudo code :
Take the input value num
index = 0
e = 0
Iterate index from 0 to num with the condition index <= num
e += 1/factorial(index)
index = index+1
Print the value of e

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

num = 10
index = 0
e = 0
while(index <= num):
    #print(index,num,e)
    e += 1/Factorial(index)
    index = index + 1
print("The value of e is :",e)

