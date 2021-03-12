'''
Problem : Every positive number can be expressed as product of ONLY prime numbers.
So for given input number ‘n’, express it as product of its prime divisors.



Example ->
 
Input : 18
Output : 2*3*3

Input : 77
Output : 7*11

Input : 300
Output : 2*2*3*5*5

'''

def Prime_Divisors_Expression_Of_Num(num):
    prime_divisors = []
    while(num != 1):
        if(num%2 == 0):
            prime_divisors.append(2)
            num = num/2
        else:
            break
    start = 3
    while(num != 1):
        if(num%start == 0):
            index = 3
            count = 0
            while(index < start):
                if(start%index == 0):
                    count += 1
                    break
                index += 2
            if(count == 0):
                prime_divisors.append(start)
            num = num/start
        else:
            start += 2
    print(prime_divisors)
    length = len(prime_divisors)
    string = ''
    index = 0
    while(index < length):
        string = string+str(prime_divisors[index])
        if(index != length-1):
            string = string+'*'
        index += 1
    return string
            
print("The primie divisors expression of given number is:",Prime_Divisors_Expression_Of_Num(19))    

