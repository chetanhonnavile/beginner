#Maximum difference in an sub array
#maximum sum

def maximum_diff(list1):
    max_diff = list1[1] - list1[0]

    for i in range(0,len(list1)):
        for j in range(i+1,len(list1)):
            if (list1[j]-list1[i]) > max_diff:
                max_diff = list1[j]-list1[i]
    return max_diff


def maximum_sum(list1):
    max_sum = list1[1] + list1[0]

    for i in range(0,len(list1)):
        for j in range(i+1,len(list1)):
            if (list1[j]+list1[i]) > max_sum:
                max_sum = list1[j]+list1[i]
    return max_sum


print maximum_diff([11,2,90,10,110])

print maximum_sum([11,2,90,121,110])
