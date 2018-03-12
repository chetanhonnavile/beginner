#common element between two lists

def ce_while(list1,list2):

    p1 = 0
    p2 = 0
    result = []
    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] == list2[p2]:
            result.append(list1[p1])
            p1 += 1
            p2 += 1
        elif list1[p1] > list2[p2]:
            p2 += 1
        else:
            p1 += 1
    return result



print ce_while([1,3,4,6,7,9,3,33],[1,2,4,5,9,10])
