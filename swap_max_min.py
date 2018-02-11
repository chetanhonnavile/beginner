# swap the max and min elements in a list


class Swapper():
    def __init__(self,list1):
        self.list1 = list1
        print "before:",list1
        index_max,index_min = list1.index(max(list1)),list1.index(min(list1))
        temp = list1[index_max]
        list1[index_max] =list1[index_min]
        list1[index_min] = temp
        print "After:",list1

   
swap_list = Swapper([99,33,6])
