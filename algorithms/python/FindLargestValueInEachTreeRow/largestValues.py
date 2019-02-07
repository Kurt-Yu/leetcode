def largestValues(self, root):
    if not root: return []
    res = []
    stack = [root]
    while stack:
        res.append(max([node.val for node in stack]))
        children = [child for node in stack for child in (node.left, node.right) if child]
        if not children: break
        stack = children
    return res