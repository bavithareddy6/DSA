#### LEETCODE question 


# Definition for a binary tree node.



# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def ischeck(self,root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2 :
            return False
        if root1.val != root2.val:
            return False
        
        
        l1=root1.left
        l2=root2.left
        r1=root1.right
        r2=root2.right

        
        flip=self.ischeck(l1,r2) and self.ischeck(r1,l2)
        notflipped=self.ischeck(l1,l2) and self.ischeck(r1,r2)
        return flip or notflipped
        

    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.ischeck(root1, root2)
    



        