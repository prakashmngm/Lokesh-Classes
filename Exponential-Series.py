'''

Problem : Exponential Series.
Input will be Positive Integers > 0.

Consider this series : x + x2 + x3 + x4 ….

Input : 2,5
Output : x + x2….+x5


List of VALID inputs : 
(1,2),(3,4),(5,6),(7,8),(4,4)

Output:
1+1^2 = 2
3+3^2+3^3+3^4 = 120

PseudoCode : 

Take input variables base and index
Initiate a variable series with 0
Iterate from 1 to index:
series += exponent(base,index)
Print the value of series

'''

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

base = 3
index = 4
series = 0
indices = 1
while(indices <= index):
    series += exponent(base,indices)
    #print(base,index,series,indices)
    indices = indices+1
print("The value of the Exponential Series is :",series)

