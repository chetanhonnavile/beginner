#Find intersection of two arrays

def intersection1(list1,list2):

    list3  = [i for i in list1 if i in list2]
    return list3

def intersection2(list1,list2):
    list3 =  list(set(list1) & set(list2))
    return list3

def intersection3(list1,list2):
    temp = set(list2)
    list3 = [i for i in list1 if i in temp]
    return list3

def intersection4(list1,list2):
    list3 = list(set(list1).intersection(list2))
    return list3

list1 = [4, 9, 1, 17, 11, 26, 28, 54, 69]
list2 = [9, 9, 74, 21, 45, 11, 63, 28, 26]

print intersection3(list1,list2)
print intersection2(list1,list2)
print intersection1(list1,list2)
print intersection4(list1,list2)
