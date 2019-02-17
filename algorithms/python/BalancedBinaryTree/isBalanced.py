def isBalanced(self, root):
    def helper(root):
        if not root: return 0
        left = helper(root.left)
        right = helper(root.right)
        if left == -1 or right == -1 or abs(left - right) > 1: return -1
        return 1 + max(left, right)
    return helper(root) != -1
    