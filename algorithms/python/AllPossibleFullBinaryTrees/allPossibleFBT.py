def allPossibleFBT(self, N):
    N -= 1
    res = []
    if N == 0: return [TreeNode(0)]
    for count in range(1, N, 2):
        for left in self.allPossibleFBT(count):
            for right in self.allPossibleFBT(N - count):
                root = TreeNode(0)
                root.left = left
                root.right = right
                res.append(root)
    return res