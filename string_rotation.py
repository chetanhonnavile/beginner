#Check if the strings are rotatable

def list_rotation(list1,list2):

    str_list1 = " ".join(map(str,list1))
    str_list2 =  " ".join(map(str,list2))

    return str_list1 in str_list2+' '+str_list2


print list_rotation([1, 1, 1, 0, 0],[1, 1, 0, 0, 1])
