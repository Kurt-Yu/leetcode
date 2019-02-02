# iterative solution

def preorder(self, root):
    if not root: return []
    stack = [root]
    res = []
    while stack:
        node = stack.pop()
        stack += node.children[::-1]
        res.append(node.val)
    return res


# recursive solution
def preorder(self, root):
    preorder = []
    
    def helper(root):
        if root:
            preorder.append(root.val)
            for node in root.children:
                helper(node)
    helper(root)
    return preorder