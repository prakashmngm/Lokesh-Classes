'''

Problem : Find all the prime divisors of input number ‘n’

Valid Inputs : 9,18,112
Valid Outputs : [3],[2,3],[2,7]

Pseudo Code:
Take the input number num
prime_divisors = []
if(num%2 == 0):
    prime_divisors.append(2)
start = 3
while(start < num):
    if(num%start == 0):
        index = 0
        count = 0
        while(index < len(prime_divisors)):
            if(start%prime_divisors[index] == 0):
                count += 1
                break
            index += 1
        if(count == 0):
            prime_divisors.append(start)
    start += 2
if(len(prime_divisors) == 0):
    return "The given number itself is a prime number"
else:
    return prime_divisors

'''

def Prime_Divisors_Of_Num(num):
    prime_divisors = []
    if(num%2 == 0):
        prime_divisors.append(2)
    start = 3
    while(start < num):
        if(num%start == 0):
            index = 0
            count = 0
            while(index < len(prime_divisors)):
                if(start%prime_divisors[index] == 0):
                    count += 1
                    break
                index += 1
            if(count == 0):
                prime_divisors.append(start)
        start += 2
    if(len(prime_divisors) == 0):
        return "The given number itself is a prime number"
    else:
        return prime_divisors
print("The prime divisors of the given number is:",Prime_Divisors_Of_Num(24))
        

