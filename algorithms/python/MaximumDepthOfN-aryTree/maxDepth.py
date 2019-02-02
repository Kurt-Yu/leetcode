def maxDepth(self, root):
    if not root: return 0
    if not root.children: return 1
    return max([1 + self.maxDepth(node) for node in root.children])