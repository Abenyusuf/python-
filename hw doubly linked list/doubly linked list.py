class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def replace(self, old_data, new_data):
        current = self.head
        while current:
            if current.data == old_data:
                current.data = new_data
                return True
            current = current.next
        return False

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


# Create an empty list
dll = DoublyLinkedList()

# Add numbers to the end of the list
dll.append(8)
dll.append(6)
dll.append(9)
dll.append(2)

# Add 0 to the beginning of the list
dll.prepend(0)

# Display the list
print("Original list:")
dll.display()

# Remove 6 and replace it with 7
dll.replace(6, 7)

# Display the modified list
print("\nModified list:")
dll.display()
