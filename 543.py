# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
    def hight(self,root):
        if root is None:
            return 0

        leftHt = self.hight(root.left)
        rightHt = self.hight(root.right)

        self.ans = max(self.ans, leftHt + rightHt)

        return max(leftHt, rightHt) + 1

      



                    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.hight(root)
        return self.ans
        