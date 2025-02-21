/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type FindElements struct {
    elements map[int]bool
}

func Constructor(root *TreeNode) FindElements {
    fe := FindElements{
        elements: make(map[int]bool),
    }
    if root != nil {
        root.Val = 0
        fe.recoverTree(root)
    }
    return fe
}

func (fe *FindElements) recoverTree(node *TreeNode) {
    if node == nil {
        return
    }
    fe.elements[node.Val] = true
    
    if node.Left != nil {
        node.Left.Val = 2*node.Val + 1
        fe.recoverTree(node.Left)
    }
    
    if node.Right != nil {
        node.Right.Val = 2*node.Val + 2
        fe.recoverTree(node.Right)
    }
}

func (fe *FindElements) Find(target int) bool {
    return fe.elements[target]
}

/**
 * Пример использования:
 * root := &TreeNode{}
 * obj := NewFindElements(root)
 * result := obj.Find(target)
 */


/**
 * Your FindElements object will be instantiated and called as such:
 * obj := Constructor(root);
 * param_1 := obj.Find(target);
 */
