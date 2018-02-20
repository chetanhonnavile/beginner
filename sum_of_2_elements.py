#Given a list ( sorted and unsorted ) ,write a program to find 2 elements which adds up to give the desired sum.



def sum_sorted_list(list1,summ):

    i = 0
    j = len(list1) -1
    while i < j:
        temp =  list1[i] + list1[j]
        if temp > summ:
            j -=1
        elif temp < summ:
            i += 1
        elif temp == summ:
            return "{0}+{1} = {2}".format(list1[i],list1[j],summ)
            break

    return "Sorted list: no 2 elements in given list add up to {0}".format(summ)


def sum_unsorted(list1,summ):

    index = 0
    list_out = []
    while index < len(list1):
        complement = summ - list1[index]

        if complement in list_out:
            return "{0}+{1} = {2}".format(list1[index],complement,summ)
        else:
            list_out.append(list1[index])
            if len(list_out) == len(list1):
                return "Unsorted list:no 2 elements in given list add up to {0}".format(summ)

        index += 1


print sum_sorted_list([1,2,3,4,4,9],8)

print sum_unsorted([30,2,9,2,1,5,4,9],111)
