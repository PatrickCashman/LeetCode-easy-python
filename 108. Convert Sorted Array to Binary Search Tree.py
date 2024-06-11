from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Helper function to recursively build the BST
        def helper(l, r):
            # Base case: if the left index exceeds the right, return None
            if l > r:
                return None

            # Find the middle element of the current subarray
            m = (l + r) // 2
            # Create a new TreeNode with the middle element
            root = TreeNode(nums[m])
            # Recursively build the left subtree using the left half of the current subarray
            root.left = helper(l, m - 1)
            # Recursively build the right subtree using the right half of the current subarray
            root.right = helper(m + 1, r)
            return root

        # Call the helper function with the entire array
        return helper(0, len(nums) - 1)
    
#time: O(n)
#space: O(log n)

def print_tree_inorder(root):
    if root:
        print_tree_inorder(root.left)
        print(root.val, end=' ')
        print_tree_inorder(root.right)

nums = [-10,-3,0,5,9]
solution_instance = Solution()
root = (solution_instance.sortedArrayToBST(nums))

print(f"Inorder Traversal of the Tree:"); print_tree_inorder(root)
