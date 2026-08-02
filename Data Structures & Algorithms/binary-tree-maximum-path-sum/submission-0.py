# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans=float('-inf')
        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            lt=dfs(node.left)
            rt=dfs(node.right)
            temp=max(node.val,node.val+lt, node.val+rt)
            ans=max(ans,lt+node.val+rt,temp)
            return temp
        dfs(root)
        return ans

        