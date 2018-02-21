def selection_sort(list1):
    """ divides the list into two categories ,sort and unsorted.
       identify the smallest item and swap with first item of the list
       not fast
       """

    for i in range(0,len(list1)-1):

        minIndex = i

        for j in range(i+1,len(list1)):
            if list1[j] < list1[minIndex]:
                minIndex= j
                print "minindex",j

        if minIndex != i:
            list1[i],list1[minIndex] = list1[minIndex],list1[i]
    return list1

print selection_sort([99,9999,3,3,5,8,11,1,2,6,10,0,])



