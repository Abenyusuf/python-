class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not isinstance(key, Node):
            key = Node(key)
        if self.root is None:
            self.root = key
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, root, key):
        if root.key < key.key:
            if root.right is None:
                root.right = key
            else:
                self._insert_recursive(root.right, key)
        else:
            if root.left is None:
                root.left = key
            else:
                self._insert_recursive(root.left, key)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, root, key):
        if root is None or root.key == key:
            return root
        if root.key < key:
            return self._search_recursive(root.right, key)
        return self._search_recursive(root.left, key)

    def showtree(self):
        return self._showtree_recursive(self.root)

    def _showtree_recursive(self, root):
        if root is not None:
            self._showtree_recursive(root.left)
            print(root.key)
            self._showtree_recursive(root.right)


# Main program
# create empty tree
tree = BinarySearchTree()

# accept values for the bst
# 45 3 5 6
node_values = input('Enter the values for the nodes with spaces in between: ')

# loop through the values to create the nodes
for value in node_values.split():
    new_node = Node(int(value))
    tree.insert(new_node)

print("Binary Search Tree:")
tree.showtree()

search_key = int(input('Enter a value to search: '))

found_node = tree.search(search_key)
if found_node is not None:
    print('Found node with key =', found_node.key)
else:
    print('Key not found')