from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: if the tree is empty, the depth is 0
        if not root:
            return 0

        # The depth of the tree rooted at 'root' is 1 (for the root itself)
        # plus the maximum of the depths of the left and right subtrees
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
#time: O(n)
#space: O(h)
   
root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))

solution = Solution()
print(solution.maxDepth(root))