# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(node):
            # Base case: null node
            if not node:
                return None
            
            # Если текущий узел равен p или q, возвращаем этот узел.
            # Это означает, что нашли один из искомых узлов.
            if node == p or node == q:
                return node
            
            # Recur for left and right children
            left = dfs(node.left)
            right = dfs(node.right)
            
            # Если оба вызова (левый и правый) вернули непустые значения, это означает, что узлы p и q
            # находятся в разных поддеревьях текущего узла.
            # Следовательно, текущий узел (node) является наименьшим общим предком (LCA).

            if left and right:
                return node
            
            # Если только один из вызовов (левый или правый) вернул непустое значение, возвращаем его.
            # Это означает, что либо нашли один из узлов (p или q), либо их общий предок 
            # уже найден в этом поддереве.
            # Если оба вызова вернули None, возвращаем None.

            return left if left else right
        
        # Start the DFS from the root
        return dfs(root)
