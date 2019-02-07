def invertTree(self, root):
    if not root: return None
    if not root.left and not root.right: return root
    root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
    return root