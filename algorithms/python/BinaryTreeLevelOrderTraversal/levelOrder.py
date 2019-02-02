def levelOrder(self, root):
    if not root: return []
    stack = [[root]]
    while True:
        children = [child for node in stack[-1] for child in (node.left, node.right) if child]
        if not children: break
        stack.append(children)
    res = []
    for level in stack:
        temp = [node.val for node in level]
        res.append(temp)
    return res