'''

Given a number, find its largest divisor. Such that largest factor is not number itself.
Input number > 1

Valid Inputs : 7, 22,111
Valid Outputs : 1, 11, 37

Pseudo Code:
Take the input number(num)
divisor = 2
Iterate the loop with condition num >= divisor
if(num%divisor == 0)
largest = num/divisor
Break
divisor += 1
print(largest)

'''
def largest_factor(num):
    divisor = 2
    while(num >= divisor):
        if(num%divisor == 0):
            largest = num//divisor
            break
        divisor += 1
    return largest
print("The largest factor of the given number is :",largest_factor(1024))
