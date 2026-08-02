# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        tar=0
        def dfs(node):
            nonlocal tar
            if not node:
                return
                
            lt=dfs(node.left)
            if lt is not None:
                return lt
            tar+=1
            if tar==k:
                return node.val
            rt=dfs(node.right)
            if rt is not None:
                return rt
            
            
        return dfs(root)
