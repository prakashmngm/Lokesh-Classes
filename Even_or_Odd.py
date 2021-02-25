'''

Problem : Even/Odd

Input : A number.( integers + decimals )
Output : Whether the number is even or odd.


Pseudo Code : 
1 . input a number
	1.a) check if the number is integer or not.
Find the modulus of the number by dividing it with 1
If the modulus is 0 then the number is integer
If the modulus is not 0 then the number is decimal
1.b) if integer, go to step 2)
1.c)if not integer, say - “Invalid Number”.  Go to step 5).


2 . find the modulus of the number by dividing it with 2
3 . if the modulus is 1 then the number is a odd number
4 . if the modulus is 0 then the number is a even number 
5. End.


'''

n = 99.009
r1 = n%1
if(r1 == 0):
    r2 = n%2
    print(r2)
    if(r2 == 0):
        print("The given number is even \n")
    else:
        print("The given number is odd \n")
else:
    print("The given number is decimal and can't be decided as odd or even \n")




