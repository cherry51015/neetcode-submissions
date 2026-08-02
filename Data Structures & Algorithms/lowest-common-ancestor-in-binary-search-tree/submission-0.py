# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return 
            if node.val==p.val or node.val==q.val:
                return node
            lt=dfs(node.left)
            rt=dfs(node.right)
            if lt and rt:
                return node
            elif lt:
                return lt
            else:
                return rt
        return dfs(root)


        