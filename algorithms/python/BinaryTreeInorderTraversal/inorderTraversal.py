def inorderTraversal(self, root):
    inorder = []
    def helper(root):
        if root:
            helper(root.left)
            inorder.append(root.val)
            helper(root.right)
    helper(root)
    return inorder