# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q=deque([])
        q.append((root,1))
        ans=float('-inf')
        while q:
            node,l=q.popleft()
            if node.left:
                q.append((node.left,l+1))
            if node.right:
                q.append((node.right,l+1))

            ans=max(ans,l)
        return ans
        
        