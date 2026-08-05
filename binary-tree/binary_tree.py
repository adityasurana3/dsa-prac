class Node:
    def __init__(self, val):
        self.root = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def set_root(self, val):
        self.root = Node(val)
        return self.root

    def append_left(self, parent, val):
        node = Node(val)
        if self.root is None:
            print("Please set the root first")
            return None
        if parent.left is None:
            parent.left = node
        return parent.left

    def append_right(self, parent, val):
        node = Node(val)
        if parent.right is None:
            parent.right = node
        return parent.right


tree = BinaryTree()

root = tree.set_root(10)
left = tree.append_left(root, 5)
right = tree.append_right(root, 15)

tree.append_left(left, 3)
tree.append_right(left, 7)
