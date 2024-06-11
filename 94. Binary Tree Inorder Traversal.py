from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        current_pointer = root

        # Iterative in order traversal
        while current_pointer or stack:
            # Traverse to the leftmost node
            while current_pointer:
                stack.append(current_pointer)
                current_pointer = current_pointer.left

            # current_pointer is now None, backtrack using the stack
            current_pointer = stack.pop()
            # Visit the node
            result.append(current_pointer.val)
            # Move to the right subtree
            current_pointer = current_pointer.right

        return result

#time: O(n)
#space: O(n)

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

solution = Solution()
print(solution.inorderTraversal(root))