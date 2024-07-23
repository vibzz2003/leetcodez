# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def maxpathsumhelper(node: TreeNode) -> int:
            nonlocal maxsum
            if not node:
                return 0

            leftsum = max(0, maxpathsumhelper(node.left))
            rightsum = max(0, maxpathsumhelper(node.right))

            sumvalue = node.val + leftsum + rightsum

            maxsum = max(maxsum, sumvalue)

            return node.val + max(leftsum, rightsum)
        
        maxsum = float('-inf')
        maxpathsumhelper(root)
        return maxsum