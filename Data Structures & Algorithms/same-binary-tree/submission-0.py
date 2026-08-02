# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        list1=[]
        list2=[]
        def dfs(node,mylist):
            if not node:
                return mylist.append("null")
            mylist.append(node.val)
            dfs(node.left,mylist)
            dfs(node.right,mylist)
            return mylist
        return True if dfs(p,list1)==dfs(q,list2) else False
    
            
        