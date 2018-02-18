class is_rotate():

    def __init__(self,list1,list2):

        self.list1 = list1
        self.list2 = list2
        if len(list1) != len(list2) and set(list1) != set(list2):
            print  "Rotation False"
        else:
        #find the index of list1's first element in list2
            d = list2.index(list1[0])
            new = list2[d:]+list2[:d]
            if new == list1:
                 print "rotation true"

    def rotate(self):
        if len(self.list1) != len(self.list2) and set(self.list1) != set(self.list2):
            return False
        else:
            # find the index of list1's first element in list2
            d = self.list2.index(self.list1[0])
            new = self.list2[d:] + self.list2[:d]
            if new == self.list1:
                return True
            else:

                return False

    def rotater(self,list3,list4):
        if len(list3) != len(list4) and set(list3) != set(list4):
            return False
        list3= list3
        list4 = list4
        # find the index of list1's first element in list2
        d = list4.index(list3[0])
        new = list4[d:] + list4[:d]
        if new == list3:
            return True
        else:

            return False


obj = is_rotate([1,2,3,4,5,6,7],[4,5,6,7,1,2,3])

print obj.rotate()

print obj.rotater([6,7,8,9,0],[9,0,1,6,7,8])

