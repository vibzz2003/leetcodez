# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        
        list1 = []

        def inorder(node):
            if node is not None:
                inorder(node.left)
                list1.append(node.val)
                inorder(node.right)
            
        inorder(root)

        for i in range(len(list1)):
            num = list1[k-1]
        
        return num