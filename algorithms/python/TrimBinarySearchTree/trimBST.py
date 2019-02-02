def trimBST(self, root, L, R):
    dummy = TreeNode(0)
    
    def helper(root):
        if not root: return None
        if L <= root.val <= R:
            root.left = helper(root.left)
            root.right = helper(root.right)
            return root
        elif root.val < L:
            return helper(root.right)
        else:
            return helper(root.left)
    
    dummy.left = helper(root)
    return dummy.left