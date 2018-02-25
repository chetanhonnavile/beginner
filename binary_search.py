import random
def search_binary(list1,x):
    print list1
    print x
    low = 0
    high = len(list1)-1
    while low < high:
        mid = (low+high)/2
        if x == list1[mid]:
            return mid
        elif x < list1[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return "Element not found"


list1 = [random.randint(0,100) for _ in range(10)]

print search_binary(list1,random.randint(0,100))
