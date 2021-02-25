'''

Problem : Shifting of variables two one position

What we did was : a->b->

What we will do :  a->b->c->

Input : a=5, b=10, c=100

Output : a=100, b=5, c=10
			

Pseudo Code : 


t1 = b
b = a
a = c
c = t1

a b c
b c a


'''

a=5
b=10
c=100
print(a,b,c)
t1 = a
a = b
b = c
c = t1
print(a,b,c)



