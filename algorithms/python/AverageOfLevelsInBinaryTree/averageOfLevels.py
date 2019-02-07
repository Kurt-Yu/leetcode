def averageOfLevels(self, root):
    if not root: return []
    stack = [root]
    res = []
    while stack:
        res.append(sum([node.val for node in stack]) / len(stack))
        children = [child for node in stack for child in (node.left, node.right) if child]
        if not children: break
        stack = children
    return res