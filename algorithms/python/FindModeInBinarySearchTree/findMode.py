def findMode(self, root):
    if not root: return []
    count = {}
    
    def helper(root):
        if root:
            count[root.val] = count.get(root.val, 0) + 1
            helper(root.left)
            helper(root.right)
    helper(root)
    m = max(count.values())
    return [key for key, v in count.items() if v == m]