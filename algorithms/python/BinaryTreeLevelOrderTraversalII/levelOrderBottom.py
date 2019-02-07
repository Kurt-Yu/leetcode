def levelOrderBottom(self, root):
    if not root: return []
    
    stack = [[root]]
    while True:
        children = [child for node in stack[-1] for child in (node.left, node.right) if child]
        if not children: break
        stack.append(children)
    
    for level in stack:
        for i in range(len(level)):
            level[i] = level[i].val
    stack.reverse()
    return stack