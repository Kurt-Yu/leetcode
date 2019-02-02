# Method 1: recursive solution:
def insertIntoBST(self, root, val):
    res = root
    def helper(root, val):
        if root:
            if root.val < val:
                if root.right: helper(root.right, val)
                else: root.right = TreeNode(val)
            else:
                if root.left: helper(root.left, val)
                else: root.left = TreeNode(val)
    helper(root, val)
    return res
    

# Method 2: iterative solution
def insertIntoBST(self, root, val):
    if not root: return TreeNode(val)
    curr = root
    while True:
        if curr.val < val:
            if curr.right:
                curr = curr.right
            else:
                curr.right = TreeNode(val)
                break
        else:
            if curr.left:
                curr = curr.left
            else:
                curr.left = TreeNode(val)
                break
    return root