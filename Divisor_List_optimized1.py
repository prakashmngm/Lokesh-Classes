'''
Implement the optimization largest divisor problem.

Valid Inputs : 9,12,961
Valid Outputs : [1,9,3],[1,12,2,6,3,4],[1,961,31]

Pseudo Code:
Take the input num
divisor = 1
divisor_list = []
sq_root = sqrt(num)
Iterate the loop with condition divisor <= sq_root
if(num%divisor == 0)
Append divisor to the list
pair_divisor = num/divisor
if(pair_divisor != divisor)
Append pair_divisor the list
divisor += 1


'''

def divisor_list(num):
    divisor = 1
    divisor_list = []
    sq_root = num**0.5
    while(divisor <= sq_root):
        if(num%divisor == 0):
            divisor_list.append(divisor)
            pair_divisor = num//divisor
            if(pair_divisor != divisor):
                divisor_list.append(pair_divisor)
        divisor += 1
    return divisor_list
print("The divisor list of the given number is:",divisor_list(100))
                    
            

