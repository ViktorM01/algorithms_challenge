# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def find(root, ans):
            if root is not None: 
                find(root.left, ans)
                find(root.right, ans)
                ans.append(root.val)

        ans = []
        find(root, ans)
        return ans
