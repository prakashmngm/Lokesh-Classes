'''
Take the input number num
length = length(num)
sum = 0
index = 1
Iterate the loop with condition num>0
digit = num%10
sum += (digit*exponent(10,length-index))
sum += digit*(10**(length-index))
num = num//10
index += 1
print(“The reverse of the given number is:”,sum)

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


num = 647638
length = length(num)
summ = 0
index = 1
while(num > 0):
    digit = num%10
    summ += (digit*exponent(10,(length-index)))
    num = num//10
    index += 1
print("The reverse of the given number is:",summ)

