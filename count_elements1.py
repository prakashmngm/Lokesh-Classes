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
    marks = [marks0,marks1,marks2,marks3,marks4,marks5,marks6,marks7,marks8,marks9,marks10]
    for ele in list1:
        if(ele == 0):
            marks[0] += 1
        elif(ele == 1):
            marks[1] += 1
        elif(ele == 2):
            marks[2] += 1
        elif(ele == 3):
            marks[3] += 1
        elif(ele == 4):
            marks[4] += 1
        elif(ele == 5):
            marks[5] += 1
        elif(ele == 6):
            marks[6] += 1
        elif(ele == 7):
            marks[7] += 1
        elif(ele == 8):
            marks[8] += 1
        elif(ele == 9):
            marks[9] += 1
        else:
            marks[10] += 1
    index = 0
    while(index < len(marks)):
        print('marks('+str(index)+') :',marks[index])
        index += 1
        
print(Count_Elements([2, 5, 7, 1, 3, 2, 1, 5, 6, 2, 9]))


