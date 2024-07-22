# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        #preorder = root->left->right

        #right child pointer -> points to the next node
        #left child pointer -> always null

        if not root:
            return None
        
        # queue = [root]

        # while queue:
        #     size = len(queue)

        #     for i in range(size):
        #         node = queue.pop(0)

        #         if i < size - 1:
        #             node.left = None
        #             node.right = queue[0]

        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        # this cannot be done as we are using bfs here while we need to do dfs and preorder traversal to maintain the node sequence
        # use stacks 

        stack = [root]

        while stack:
            node = stack.pop()

            if node.right:
                stack.append(node.right)
            
            if node.left:
                stack.append(node.left)
            
            if stack:
                node.right = stack[-1] #pointing to top of the stack
            
            node.left = None

            