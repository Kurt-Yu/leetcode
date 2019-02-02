def leafSimilar(self, root1, root2):
    def helper(root, res):
        if root:
            helper(root.left, res)
            if not root.left and not root.right: res.append(root.val)
            helper(root.right, res)
        
    self.res1 = []
    self.res2 = []
    helper(root1, self.res1)
    helper(root2, self.res2)
    return self.res1 == self.res2