'''
Implement the optimization largest divisor problem.

Valid Inputs : 9,12,961
Valid Outputs : [1,9,3],[1,12,2,6,3,4],[1,961,31]

Pseudo Code:
Take the input num
divisor = 1
divisor_list = []
Iterate the loop until it breaks
if(num%divisor == 0)
if(divisor in divisor_list)
break
else
Append divisor to the list
pair_divisor = num/divisor
if(pair_divisor != divisor)
Append pair_divisor the list
divisor += 1


'''

def largest_divisor(num):
    divisor = 1
    divisor_list = []
    while(1):
        if(num%divisor == 0):
            if(divisor in divisor_list):
                break
            else:
                divisor_list.append(divisor)
                pair_divisor = num//divisor
                if(pair_divisor != divisor):
                    divisor_list.append(pair_divisor)
        divisor += 1
    return divisor_list
print("The divisor list of the given number is:",largest_divisor(2000))
                    
            

