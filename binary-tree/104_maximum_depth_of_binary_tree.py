from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.height = 0

    def helper(self, root: Optional[TreeNode], count: int) -> None:

        if root is None:
            self.height = max(self.height, count)
            return
        self.helper(root.left, count + 1)
        self.helper(root.right, count + 1)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.helper(root=root, count=0)
        return self.height

    def maxDepthBFS(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        queue = deque([])
        queue.append(root)
        count = 0
        while queue:
            que_len = len(queue)
            for _ in range(que_len):
                e = queue.popleft()
                if e.left is not None:
                    queue.append(e.left)
                if e.right is not None:
                    queue.append(e.right)
            count += 1

        return count


# root = [3, 9, 20, None, None, 15, 7]
root = TreeNode(3)
root1 = TreeNode(9)
root2 = TreeNode(20)
root3 = TreeNode(None)
root4 = TreeNode(None)
root5 = TreeNode(15)
root6 = TreeNode(7)

root.left = root1
root.right = root2
root2.left = root5
root2.right = root6
root1.left = None
root1.right = None


s = Solution()
print(s.maxDepth(root))
print(s.maxDepthBFS(root))
