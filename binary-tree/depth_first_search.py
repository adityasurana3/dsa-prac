class DfsInBt:
    def pre_order(self, node: "BT"):
        # root -> left -> right
        if node is None:
            return

        print(node.val)
        self.pre_order(node.left)
        self.pre_order(node.right)

    def in_order(self, node):
        # left -> root -> right
        if node is None:
            return
        self.in_order(node.left)
        print(node.val)
        self.in_order(node.right)

    def post_order(self, node):
        # left -> right -> root
        if node is None:
            return
        self.post_order(node.left)
        self.post_order(node.right)
        print(node.val)


class BT:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def tree(self, node):
        pass


node1 = BT(5)
node2 = BT(3)
node3 = BT(4)
node4 = BT(2)
node5 = BT(9)
node6 = BT(8)
node7 = BT(10)
node8 = BT(1)
node9 = BT(6)


node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
node6.left = node8
node6.right = node9


dfs = DfsInBt()
# dfs.pre_order(node1)
# dfs.in_order(node1)
dfs.post_order(node1)
