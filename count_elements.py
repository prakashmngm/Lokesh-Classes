'''
Count the elements of the given list

'''

def Count_Elements(list1):
    
    marks0 = 0
    marks1 = 0
    marks2 = 0
    marks3 = 0
    marks4 = 0
    marks5 = 0
    marks6 = 0
    marks7 = 0
    marks8 = 0
    marks9 = 0
    marks10 = 0
    for ele in list1:
        if(ele == 0):
            marks0 += 1
        elif(ele == 1):
            marks1 += 1
        elif(ele == 2):
            marks2 += 1
        elif(ele == 3):
            marks3 += 1
        elif(ele == 4):
            marks4 += 1
        elif(ele == 5):
            marks5 += 1
        elif(ele == 6):
            marks6 += 1
        elif(ele == 7):
            marks7 += 1
        elif(ele == 8):
            marks8 += 1
        elif(ele == 9):
            marks9 += 1
        else:
            marks10 += 1
    print(marks0,'\n',marks1,'\n',marks2,'\n',marks3,'\n',marks4,'\n',marks5,'\n',marks6,'\n',marks7,'\n',marks8,'\n',marks9,'\n',marks10)


print(Count_Elements([2, 5, 7, 1, 3, 2, 1, 5, 6, 2, 9]))


