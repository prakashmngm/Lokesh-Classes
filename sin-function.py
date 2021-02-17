'''
sin(x) =   x^1/1!   -    x^3/3!   +   x^5/5!   - x^7/7!  +   …..

Input : x, n ( No. of terms I want in series )

Input : 3.14, 10

Output : sin(3.14) = sin(180) = 0

Radians vs Degrees


( 0, 30, 60, 90 ….)
2pi = 360
Pi = 180


Pseudo code :
1.Take input variables radians,num
2. sin = 0
3. Indices = 1
4. odd = 1
4. Iterate indices from 1 to num with condition index <= num
	If index%2 == 1
    sin =  sin + exponent(radians,odd)/factorial(odd)
    If index%2 == 0
	sin = sin - exponent(radians,odd)/factorial(odd)
    Index += 1
    odd += 2
5 . print the value of th sin

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

def factorial(num):
    if(num == 0):
        return 1
    else:
        fact = 1
        index =1
        while(index <= num):
            fact *= index
            index = index+1
        return fact


radians = 3*3.14159/2
num = 15
sin = 0
index = 1
odd = 1
while(index <= num):
    if(index%2 == 1):
        sin =  sin + (exponent(radians,odd)/factorial(odd))
    if(index%2 == 0):
        sin = sin - (exponent(radians,odd)/factorial(odd))
    index += 1
    odd += 2
print("The value of sin for the given radians is :",sin)
