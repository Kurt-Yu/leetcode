def distributeCoins(self, root: 'TreeNode') -> 'int':
    self.res = 0
    def helper(root):
        if not root: return 0
        left = helper(root.left)
        right = helper(root.right)
        self.res += abs(left) + abs(right)
        return root.val + left + right - 1
    helper(root)
    return self.res