from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base case if both trees are empty
        if not p and not q:
            return True 
        # Base case if one tree is empty or values are not the same
        if not p or not q or p.val != q.val:
            return False

        # Recursion if a return statment hasn't been reached yet
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))

#time: O(p + q)
#space: O(h), where h is the height of the tree

tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)

tree2 = TreeNode(1)
tree2.left = TreeNode(2)
tree2.right = TreeNode(3)

solution = Solution()
print(solution.isSameTree(tree1, tree2))


