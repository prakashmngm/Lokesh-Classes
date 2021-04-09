def common_words(string1,string2):
    string1_list = string1.split(' ')
    string2_list = string2.split(' ')
    string1_words_only = []
    string2_words_only = []
    count = 0
    for ele1 in string1_list:
        for ele2 in string2_list:
            flag = 0
            if(ele1 == ele2):
                count += 1
                flag = 1
                break
        if(flag != 1):
            string1_words_only.append(ele1)
    for ele2 in string2_list:
        for ele1 in string1_list:
            flag = 0
            if(ele2 == ele1):
                flag = 1
                break
        if(flag != 1):
            string2_words_only.append(ele2)
    return count,string1_words_only,string2_words_only
    
string1 = 'The first column F will contain only 5 unique values'
string2 = 'The second column S will contain only 3 unique values'
print("The common words"+'\t'+"words in string1 only"+'\t'+"words in string2 only"+'\t'"are:",common_words(string1,string2))
