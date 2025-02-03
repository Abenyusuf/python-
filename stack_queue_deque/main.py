from stack import stack
from queue import queue

number_stack = stack()

number_stack.push(65)
number_stack.push(0)
number_stack.push(4)

node = number_stack.my_stack.head
while node != None:
    print(node.data, end='')
    node = node.next
print()

item = number_stack.pop()
print('we popped', item)


number_queue = queue()
number_queue.enqueue(1)
number_queue.enqueue(2)
number_queue.enqueue(3)
number_queue.enqueue(4)

print("queue implementation")
node = number_queue.my_queue.head
while node != None:
    print(node.data, end='')
    node = node.next
print()

