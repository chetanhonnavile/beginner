def bubble_sort(list1):

    for j in range(len(list1)-1,0,-1):
        for i in range(j):

            if list1[i] > list1[i+1]:

                temp = list1[i]
                list1[i] = list1[i+1]
                list1[i+1] = temp


list1 =[4,3,2,1]
bubble_sort(list1)
print(list1)


