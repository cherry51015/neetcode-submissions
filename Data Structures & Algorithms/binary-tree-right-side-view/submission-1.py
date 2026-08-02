# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q=deque([root])
        ans=[]
        while q:
            n=len(q)
            while n!=1:
                node=q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                n-=1
            lnode=q.popleft()
            ans.append(lnode.val)
            if lnode.left:
                q.append(lnode.left)
            if lnode.right:
                q.append(lnode.right)
        return ans
             
            

            
        