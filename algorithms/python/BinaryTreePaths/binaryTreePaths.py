# Method 1: iterative solution
def binaryTreePaths(self, root: 'TreeNode') -> 'List[str]':
    if not root: return []
    res, stack = [], [(root, str(root.val))]
    while stack:
        node, string = stack.pop()
        if not node.left and not node.right:
            res.append(string)
        if node.right:
            stack.append((node.right, string + "->" + str(node.right.val)))
        if node.left:
            stack.append((node.left, string + "->" + str(node.left.val)))
    return res

# Method 2: recursive solution
def binaryTreePaths(self, root: 'TreeNode') -> 'List[str]':
    res = []
    def helper(root, ls):
        if not root: return ""
        if not root.left and not root.right:
            res.append(ls + str(root.val))
        helper(root.left, ls + str(root.val) + "->")
        helper(root.right, ls + str(root.val) + "->")
    helper(root, "")
    return res