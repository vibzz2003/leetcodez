# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(node:TreeNode, current_sum: int)->int:
            if not node:
                return 0
            
            current_sum = current_sum *10 + node.val

            if not node.left and not node.right:
                return current_sum
            
            left_sum = helper(node.left, current_sum)
            right_sum = helper(node.right, current_sum)

            return left_sum + right_sum
        
        return helper(root, 0)