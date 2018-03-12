def most_freq_item(myList):

    max_count = 0
    max_item = None
    count = {}


    for item in myList:
        if item not in count:
            count[item] = 1
        else:
            count[item] += 1

        if count[item] > max_count:
            max_count = count[item]
            max_item = item


    return max_item


print most_freq_item([1,2,3,2,4,5,6,7,3,2,1,'a','a','a','a'])
