'''

Find list of all prime numbers between ‘n’ and ‘m’.
The values of ‘n’ and ‘m’ will be given as input.

Valid inputs : (2,10),(10,50),(50,100)
Valid Outputs : [3,7],[11,13,17,19,23,29,31,37,41,43,47],[53,59,61,67,71,73,79,83,89,97]

Pseudo Code:
Take input numbers num1 and num2
if(num1%2 == 0)
start = num1+1
else
start = num1+2
prime_list = [2]
Iterate the loop with condition start < num2
index = 0
count = 0
Iterate the loop with condition len(prime_list) > index
if(start%prime_list[index] == 0)
count += 1
break
index += 1
if(count == 0)
prime_list.append(start)
start += 2


'''

def Prime_Numbers_Between_Num1_Num2(num1,num2):
    if(num1 == 2):
        start = 3
    elif(num1%2 == 0):
        start = num1+1
    else:
        start = num1+2
    prime_list = []
    while(start < num2):
        index = 3
        count = 0
        while(index < start):
            if(start%index == 0):
                count += 1
                break
            index += 2
        if(count == 0):
            prime_list.append(start)
        start += 2
    return prime_list
print("The prime numbers between 9 and 100 are:",Prime_Numbers_Between_Num1_Num2(10,100))

