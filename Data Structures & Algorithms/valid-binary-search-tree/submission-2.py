# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node,l,h):
            if not node:
                return True
            if node.val<=l or node.val>=h:
                return False
            
            lt=dfs(node.left,l,node.val)
            rt=dfs(node.right,node.val,h)
            return lt and rt
        
        return dfs(root,float('-inf'),float('inf'))

            
            

            