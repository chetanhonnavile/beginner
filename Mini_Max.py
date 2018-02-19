#!/usr/bin/python

class MiniMax:

    """ find the first two maximum and minimum elements from a list"""

    def __init__(self,list2):

        self.list2 = list2

        list2 = list(set(list2))
        first_min = list2.pop(list2.index(min(list2)))
        second_min = list2.pop(list2.index(min(list2)))

        print  "Using Index and pop methods: Min_1:{0}  min_2:{1}".format(first_min,second_min)

    def largest(self):

        if self.list2[0] > self.list2[1]:
            first_largest = self.list2[0]
            second_largest = self.list2[1]

        else:
            first_largest = self.list2[1]
            second_largest = self.list2[0]

        for i in range(2,len(self.list2)):
            if self.list2[i] > first_largest:
                second_largest = first_largest
                first_largest = self.list2[i]
            elif self.list2[i] > second_largest:
                second_largest = self.list2[i]
            else:
                pass

        return "Maxima:" ,first_largest,second_largest


    def smallest(self):


        if self.list2[0] < self.list2[1]:
            first_smallest = self.list2[0]
            second_smallest  = self.list2[1]

        else:
            first_smallest= self.list2[1]
            second_smallest = self.list2[0]

        for i in range(2,len(self.list2)):
            if self.list2[i] < first_smallest:
                second_smallest = first_smallest
                first_smallest = self.list2[i]
            elif self.list2[i] < second_smallest:
                second_smallest = self.list2[i]

            else:
                pass

        return "Minima:",first_smallest,second_smallest



obj = MiniMax([11,22,33,111,12,902,223,999,])

print "--------Using for loops---------"
print obj.largest()
print obj.smallest()
