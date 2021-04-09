def compute_conditional_probability(string,lst):
    list1 = string.split('|')
    f = list1[0]
    s = list1[1]
    length = len(lst)
    s_count = 0
    f_count = 0
    s_index = 1
    f_index = 0
    for index in range(length):
        if(s == lst[index][s_index]):
            s_count += 1
            if(f == lst[index][f_index]):
                f_count += 1
    probability = f_count/s_count
    return probability

lst = [['F1','S1'],['F2','S2'],['F3','S3'],['F1','S2'],['F2','S3'],['F3','S2'],['F2','S1'],['F4','S1'],['F4','S3'],['F5','S1']]
print("The probability of given condition is:",compute_conditional_probability('F2|S1',lst))
