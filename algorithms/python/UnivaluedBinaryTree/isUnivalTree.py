# Method 1: traversal the tree and check if all the node has the same value

def isUnivalTree(self, root):
    preorder = []
    def helper(root):
        if root:
            preorder.append(root.val)
            helper(root.left)
            helper(root.right)
    helper(root)
    return len(set(preorder)) == 1


# Method 2: recursively call the function
def isUnivalTree(self, root):
    if not root: return True
    if root.left:
        if not root.left.val == root.val: return False
    if root.right:
        if not root.right.val == root.val: return False
    return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)