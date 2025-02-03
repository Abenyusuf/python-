from LinkedList import LinkedList
from Node import Node


class Deque:
    def __init__(self):
        self._list = LinkedList()

    def push_front(self, data):
        self._list.prepend(Node(data))

    def push_back(self, data):
        self._list.append(Node(data))

    def pop_front(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        data = self._list.head.data
        self._list.remove_after(None)  # Removing head
        return data

    def pop_back(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        if self._list.head == self._list.tail:  # If there's only one node
            data = self._list.head.data
            self._list.head = None
            self._list.tail = None
            return data
        current = self._list.head
        while current.next != self._list.tail:
            current = current.next
        data = current.next.data
        current.next = None
        self._list.tail = current
        return data

    def is_empty(self):
        return self._list.head is None
