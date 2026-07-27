from collections import deque


class BFS:
    def bfs_in_bt(self, node: "BT"):
        result = []
        queue = deque([])
        queue.append(node)
        while len(queue) != 0:
            e = queue.popleft()
            result.append(e.val)
            if e.left is not None:
                queue.append(e.left)
            if e.right is not None:
                queue.append(e.right)
        return result


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


bfs = BFS()
print(bfs.bfs_in_bt(node1))
