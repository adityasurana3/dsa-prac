from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.diff = 0

    def solve(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        leftHeight = self.solve(root.left)
        rightHeight = self.solve(root.right)
        self.diff = max(self.diff, abs(leftHeight - rightHeight))
        return 1 + max(leftHeight, rightHeight)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.solve(root)
        return self.diff <= 1


class BetterApproach:
    def solve(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        leftHeight = self.solve(root.left)
        if leftHeight == -1:
            return -1
        rightHeight = self.solve(root.right)
        if rightHeight == -1:
            return -1
        if abs(leftHeight - rightHeight) > 1:
            return -1
        return 1 + max(leftHeight, rightHeight)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        height = self.solve(root)
        return height != -1


# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(2)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(3)
# root.left.left.left = TreeNode(4)
# root.left.left.right = TreeNode(4)

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(Solution().isBalanced(root))
print(BetterApproach().isBalanced(root))
