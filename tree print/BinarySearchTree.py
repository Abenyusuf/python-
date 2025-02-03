from TreePrint import pretty_tree


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, node):
        if self.root is None:
            self.root = node
        else:
            current_node = self.root
            while current_node is not None:
                if node.key < current_node.key:
                    if current_node.left is None:
                        current_node.left = node
                        current_node = None
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = node
                        current_node = None
                    else:
                        current_node = current_node.right

    def showtree(self):
        return pretty_tree(self)

    def search(self, search_key):
        current_node = self.root
        while current_node is not None:
            if current_node.key == search_key:
                return current_node
            elif search_key < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right
        # key not found
        return None

    def remove(self, key):
        parent = None
        cur_node = self.root

        while cur_node is not None:
            # case 1 leaf node
            if cur_node.key == key:
                if cur_node.left is None and cur_node.right is None:
                    if parent is None:
                        self.root = None
                    elif parent.left is cur_node:
                        parent.left = None
                    else:
                        parent.right = None
                    return  # node not found

                # case 2: a single child of the current node
                if cur_node.left is not None and cur_node.right is None:
                    if parent is None:
                        self.root = cur_node.left
                    elif parent.left is cur_node:
                        parent.left = cur_node.left
                    else:
                        parent.right = cur_node.left
                    return  # node not found

                # case 2 : right child scenario
                elif cur_node.left is None and cur_node.right is not None:
                    if parent is None:
                        self.root = cur_node.right
                    elif parent.left is cur_node:
                        parent.left = cur_node.right
                    else:
                        parent.right = cur_node.right
                    return
                    # node not found

                # case 3
                else:
                    # find successor leftmost child of the right subtree
                    successor = cur_node.right
                    while successor.left is not None:
                        successor = successor.left  # grab leftmost child nodes

                    # copy successor to current node
                    cur_node.key = successor.key
                    parent = cur_node

                    # remove successor from the right subtree

                    cur_node = cur_node.right
                    key = parent.key  # continue loop with a new key

            elif cur_node.key < key:
                parent = cur_node
                cur_node = cur_node.right
            else:
                parent = cur_node
                cur_node = cur_node.left
        return
        # key not found
