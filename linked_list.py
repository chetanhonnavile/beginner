class Node():

    def __init__(self,data=None):
        self.data = data
        self.next_node = None

class LinkedList():

    def __init__(self):
        self.head = Node()

    def append(self,data):
        #create a new node
        new_node = Node(data)

        current_node = self.head
        while current_node.next_node != None:

            current_node = current_node.next_node
        current_node.next_node = new_node

    def length(self):
        current_node = self.head
        count = 0
        while current_node.next_node != None:
            count += 1
            current_node = current_node.next_node

        return "length:",count

    def display(self):

        current_node = self.head
        elements = []
        while current_node.next_node != None:
            current_node = current_node.next_node
            elements.append(current_node.data)
        return 'elements',elements


    def get(self,index):
        if index >= self.length():
            return "bad index"
        current_node = self.head
        cur_idx = 0

        while True:
                current_node = current_node.next_node
                if cur_idx == index:
                    return current_node.data
                cur_idx += 1


    def erase(self,index):
        if index >= self.length():
            return "bad index"
        cur_idx = 0
        current_node = self.head
        while True:
            last_node = current_node
            current_node = current_node.next_node
            if cur_idx == index:
                last_node.next_node = current_node.next_node
                return
            cur_idx += 1










my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
print my_list.display()
print my_list.length()
print my_list.get(2)
print my_list.erase(1)
print my_list.display()
