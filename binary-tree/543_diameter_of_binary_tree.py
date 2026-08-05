from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def solve(self, root: Optional[TreeNode]) -> tuple[int, int]:
        if root is None:
            return 0, 0
        leftHeight, leftDiameter = self.solve(root.left)
        rightHeight, rightDiameter = self.solve(root.right)
        height = 1 + max(leftHeight, rightHeight)
        diameter = leftHeight + rightHeight
        return height, max(leftDiameter, rightDiameter, diameter)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        _, diameter = self.solve(root)
        return diameter


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(Solution().diameterOfBinaryTree(root))
