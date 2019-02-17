def isCousins(self, root, x, y):
    stack = [(root, 0)]
    while stack:
        children = []
        i, j = -1, -2
        first, second = False, False
        for node, index in stack:
            if node.left:
                children.append((node.left, index * 2 + 1))
            if node.right:
                children.append((node.right, index * 2 + 2))   
            
            if node.val == x:
                i = (index - 1) // 2
                first = True
            if node.val == y:
                j = (index - 1) // 2
                second = True
            if first and second:
                return i != j  
        stack = children
    return False