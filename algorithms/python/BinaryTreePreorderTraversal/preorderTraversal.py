# Method 1: recursive solution:

def preorderTraversal(self, root):
    preorder = []

    def helper(root):
        if root:
            preorder.append(root.val)
            helper(root.left)
            helper(root.right)

    helper(root)
    return preorder

# Method 2: iterative solution
def preorderTraversal(self, root):
    if not root: return []
    stack = [root]
    res = []
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right: stack.append(node.right)
        if node.left: stack.append(node.left)
    return res