from Node import Node
from BinarySearchTree import BinarySearchTree

# create empty tree
tree = BinarySearchTree()

# accept values for the bst
# 45 3 5 6
node_values = input('enter the values for the nodes with spaces in between:')

# loop through the values to create the nodes
for value in node_values.split():
    new_node = Node(int(value))
    tree.insert(new_node)

print(tree.showtree())


node_to_remove = int(input('enter key of the node to be removed'))

tree.remove(node_to_remove)

print('updated tree after removing', node_to_remove)

print(tree.showtree())

search_key = int(input('enter a value to search:'))

found_key = tree.search(search_key)
if found_key is not None:
    print('we found node with key = %d' % found_key.key)
else:
    print('key not found')
