'''
    Problem : Modified Fibonacci Sequence

Given first three numbers of the sequence : 1, 1, 2

‘N’ number is = addition of the previous three numbers.

Input : ‘n’ ( no. of terms to print. n>0 )

Input : 5
Output : 1, 1, 2, 4, 7

---
Pseudo code :

1. Take the input variable num
2. Initiate the initial variables v1 = 1, v2 = 1, v3 = 2
3. If(num == 1) ; print(1)
4. elif(num == 2);print( 1,1)
5. elif(num == 3);print(1,1,2)
6. Else got to step 7
7. index = 1
8. summ = 0
9. print(v1,v2,v3)
10. Iterate index from 1 to num with condition index < num-2
    sum = v1+v2+v3
    v1 = v2
    v2 = v3
    v3 = sum
    print(sum)
    index += 1

'''

def Modified_Fibonacci(num):
    v1 = 0
    v2 = 1
    v3 = 1
    if(num == 1):
        print(0)
    elif(num == 2):
        print(0,1)
    elif(num == 3):
        print(0,1,1)
    else:
        index = 1
        print(v1,'\n',v2,'\n',v3)
        while(index < num-2):
            summ = v1+v2+v3
            v1 = v2
            v2 = v3
            v3 = summ
            print(summ)
            index += 1
    
Modified_Fibonacci(6)
            
    

