'''

Find list of all prime numbers less than ‘n’.
Input value ‘n’ will be > 1

Valid inputs : 5 , 9 , 10
Valid Outputs: [2,3] , [2,3,5,7] , [2,3,5,7]

Pseudo Code:
Take the input number num
start = 3
prime_list = [2]
Iterate the loop with the condition start < num
Iterate the loop with the condition len(prime_list) <= index
index = 0
count = 0
if(start%prime_list[index] == 0)
count += 1
break
index += 1
if(count == 0)
prime_list.append(start)
start += 2
print(prime_list)


'''

def Prime_Numbers_Lees_Than_Num(num):
    start = 3
    prime_list = [2]
    while(start < num):
        index = 0
        count = 0
        while(len(prime_list) > index):
            if(start%prime_list[index] == 0):
                count += 1
                break
            index += 1
        if(count == 0):
            prime_list.append(start)
        start += 2
    return prime_list
print("The prime numbers less than 100 are:",Prime_Numbers_Lees_Than_Num(100))

