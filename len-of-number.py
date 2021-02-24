'''
Take the input number num
Initiate count = 0
Iterate the loop until it reaches 0 with condition num>0
num = num/10
count += 1
Print the value of count as the number of digits in the given number

'''

def length(num):
    if(num == 0):
        return 1
    else:
        length = 0
        while(num > 0):
            num = num//10
            length += 1
        return length
print(length(56743))
