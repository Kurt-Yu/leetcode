def findBottomLeftValue(self, root):
    stack = [[root]]
    while True:
        children = [child for node in stack[-1] for child in (node.left, node.right) if child]
        if not children: return stack[-1][0].val
        stack.append(children)