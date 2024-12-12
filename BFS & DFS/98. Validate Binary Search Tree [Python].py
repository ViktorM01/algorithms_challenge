# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(root, leftMin, rightMax):
            if not root:
                return True
            
            # if current node is not greater than left child and less than right
            if not (leftMin < root.val < rightMax):
                return False 

            leftTree = validate(root.left, leftMin, root.val)
            rightTree = validate(root.right, root.val, rightMax)
            return leftTree and rightTree

        return validate(root,float("-inf"),float("inf"))
