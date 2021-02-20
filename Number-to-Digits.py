'''
Given a input number, create a list of its digits.

Input : 2343
Output : [ 2, 3, 4, 3]

Input : 200000
Output : [ 2, 0, 0, 0, 0, 0 ]

Pseudo Code:

1.Take the input variable num
2.calculate the length of the num
3.initialize a empty list digits
4.initialize index = 1
5.iterate index from 1 to length with condition index <= num
d = num/exponent(10,num-index)
Add the digit ‘d’ to the empty list ‘digits’
num = num%exponent(10,num-index)
index = index+1
6. Print the list digits

'''

num = 8762
num_str = str(num)
length = len(num_str)
digits = []
index = 1
while(index <= length):
    d = num//(10**(length-index))
    digits.append(d)
    num = num%(10**(length-index))
    index += 1
print("The list of digits of the given number is:",digits)

