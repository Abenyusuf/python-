class LinkedList:
   def __init__(self):
    self.head = none
    self.tail = none

    def append(self,new_node):
        if self.head == none:
            self.head == new_node
            self.tail == new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            
