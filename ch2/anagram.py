def anagram(str1,str2):
    result = True
    pos1 = 0
    list2 = list(str2)

    while pos1 < len(str1):
        pos2 = 0
        found = False

        while pos2 < len(list2) and not found:

            if str1[pos1] == list2[pos2]:

                found = True
            else :
                pos2 = pos2 + 1
        if found :

            list2[pos2] = None
        else :
            result = False

        pos1 = pos1 + 1

    return result

print(anagram('abcd', 'dddd'))