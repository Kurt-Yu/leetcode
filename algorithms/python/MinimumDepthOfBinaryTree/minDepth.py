def minDepth(self, root):
    if not root: return 0
    res = []
    stack = [[root]]
    level = 1
    while True:
        temp = []
        for node in stack[-1]:
            if node.left: temp.append(node.left)
            if node.right: temp.append(node.right)
            if not node.left and not node.right: res.append(level)
        if not temp: break
        level += 1
        stack.append(temp)
    return min(res)