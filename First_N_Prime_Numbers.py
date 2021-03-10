'''

Problem :
Find list of first ‘n’ prime numbers.

Valid Inputs : 5 , 9 , 10
Valid Outputs : [2,3,5,7,11],[2,3,5,7,11,13,17,19,23],[2,3,5,7,11,13,17,19,23,29]

Pseudo Code:
Take the input number
start = 3
prime_list = [2]
Iterate the loop with condition len(prime_list) <= num

count = 0
index =  0
Iterate the inner loop with condition index<len(prime_list)
if(start % prime_list[index] == 0)
	count++;
	break;


index += 1
if(count == 0)
prime_list.append(start)
start += 2

Print the prime_list

'''
def First_N_Prime_Numbers(num):
    start = 3
    prime_list = [2]
    while(len(prime_list) < num):
        count = 0
        index = 0
        while(index < len(prime_list)):
            if(start%prime_list[index] == 0):
                count += 1
                break
            index += 1
        if(count == 0):
            prime_list.append(start)
        start += 2
    return prime_list    
print("The first 25 prime numbers are :",First_N_Prime_Numbers(25))


