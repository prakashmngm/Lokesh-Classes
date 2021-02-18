'''
Problem : Fibonacci Sequence

Input : n ( no. of terms i want in the Fibonacci Sequence, n>0 )



Sample Inputs:

Input = 1
Expected Output : 1

Input = 2
Expected Output : 1, 1

Input = 3
Expected Output : 1, 1, 2

Input = 4
Expected Output : 1,1,2,3


Pseudo Code :
Take input variable num
Take start variables v1 = 1, v2 =1
sum = 0
Index = 1
print(v1,v2)
if(num == 1) ;print(num)
Else got to step 8
Iterate index from 1 to num with condition index < num-1
(5) sum = v1 + v2
(5)print(sum)
(2)v1 = v2 
(3)v2 = sum 
Index += 1

'''

num = 10
v1 = 1
v2 = 1
sum = 0
index = 1
if(num == 1):
    print(num)
else:
    print(v1,'\n',v2)
    while(index < num-1):
        sum = v1 + v2
        print(sum)
        v1 = v2
        v2 = sum
        index += 1


