'''

Problem : Implement exponential function. Input only +ve integers.

def exponential( base, index )

Input : (2,5)
Output : 32

Possible VALID  inputs : (0,3),(5,0),(0,0),(4,4), (12, 12)

If base and index is 0 , then the value of the exponent is undefined.

if base == 0 print 0. Go to step 4.

If index == 0 print 1. Go to step 4.

1. Take base and exponent values as input
2. Product = 1
2. Iterate base value to the exponent number of times and multiply the base with product in each iteration.
3. Print the value of the exponent.
4.End.


'''

def exponent(base,index):
    if((index and base) == 0):
        print("The value of the exponent is undefined")
    elif(index == 0):
        print("The value of the exponent is 1")
    elif(base == 0):
        print("The value of the exponent is 0")
    else:
        product = 1
        for indices in range(index):
            product *= base
        print("The value of the exponent is :",product)   

exponent(5,3)



