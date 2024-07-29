# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        list1 = []
        
        def inorder(node):
            if node is not None:
                inorder(node.left)
                list1.append(node.val)
                inorder(node.right)

        inorder(root)
        min_diff = float('inf')

        for i in range(1, len(list1)):
            min_diff = min(min_diff, list1[i] - list1[i-1])
        
        return min_diff


