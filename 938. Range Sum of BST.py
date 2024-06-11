from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # Base case
        if not root:
            return 0

        # If the current node's value is greater than high,
        # recurse on the left subtree (ignore the right subtree)
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)

        # If the current node's value is less than low,
        # recurse on the right subtree (ignore the left subtree)
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)

        # If the current node's value is within the range [low, high],
        # include its value and recurse on both subtrees
        return (
            root.val + 
            self.rangeSumBST(root.left, low, high) + 
            self.rangeSumBST(root.right, low, high)
        )
    
root = TreeNode(10)
root.left = TreeNode(5, TreeNode(3), TreeNode(7))
root.right = TreeNode(15)
root.right.right = TreeNode(18)

low = 7
high = 15

solution = Solution()
print(solution.rangeSumBST(root, low, high))