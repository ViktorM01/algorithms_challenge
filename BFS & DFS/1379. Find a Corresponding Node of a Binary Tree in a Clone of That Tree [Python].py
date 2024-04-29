# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        quene = deque()
        quene.append((original, cloned))

        while quene:
            orig, clone = quene.popleft()
            if orig == target:
                return clone
            if orig.left:
                quene.append((orig.left, clone.left))
            if orig.right:
                quene.append((orig.right, clone.right))
            
