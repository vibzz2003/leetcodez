# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #base
        ans = []
        if not root:
            return []
        
        queue = [root]

        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)

                if i == size-1:
                    ans.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return ans
        