def isSymmetric(self, root):
    if not root: return True
    def helper(a, b):
        if not a or not b: return a == b
        return a.val == b.val and helper(a.left, b.right) and helper(a.right, b.left)
    return helper(root.left, root.right)