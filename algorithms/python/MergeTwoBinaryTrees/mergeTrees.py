def mergeTrees(self, t1, t2):
    if t1 and t2:
        root = TreeNode(t1.val + t2.val)
        root.left = self.mergeTrees(t1.left, t2.left)
        root.right = self.mergeTrees(t1.right, t2.right)
        return root
    elif t1 and not t2:
        return t1
    elif not t1 and t2:
        return t2
    else:
        return None