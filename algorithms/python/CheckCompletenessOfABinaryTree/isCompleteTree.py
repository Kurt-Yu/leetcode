# Method 1: using level order traversal:
def isCompleteTree(self, root: 'TreeNode') -> 'bool':
    if not root: return True
    stack = [root]
    flag = False
    while stack:
        node = stack.pop(0)
        if node.left:
            stack.append(node.left)
            if flag: return False
        else: flag = True
        
        if node.right:
            stack.append(node.right)
            if flag: return False
        else: flag = True
    return True
        
# Method 2: first recursively get the size of the tree
# then use the 'index * 2 + 1' and 'index * 2 + 2' property to check completeness
def isCompleteTree(self, root: 'TreeNode') -> 'bool':
    def number(root):
        if not root: return 0
        return 1 + number(root.left) + number(root.right)
    
    size = number(root)
    def helper(root, index):
        if not root: return True
        if index >= size: return False
        return helper(root.left, index * 2 + 1) and helper(root.right, index * 2 + 2)
    return helper(root, 0)

# Method 3: 
def isCompleteTree(self, root):
    stack = [[(root, 0)]]
    layer = 0
    while True:
        children = []
        for node, value in stack[-1]:
            if node.left: children.append((node.left, 2 * value))
            if node.right: children.append((node.right, 2 * value + 1))
            if node.right and not node.left: return False
        if not children: break
        if len(stack[-1]) != pow(2, layer): return False
        stack.append(children)
        layer += 1
    return len(stack[-1]) == stack[-1][-1][1] + 1