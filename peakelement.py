#Find peak element in an array

def findpeak(list1):

    left,right = 0,len(list1)-1

    while left < right:
        mid = (left+right)//2
        if list1[mid] < list1[mid+1]:
            left = mid+1
        else:
            right = mid

    return left


list1 = [5,10,15,11,16,34,33]
print findpeak(list1)
