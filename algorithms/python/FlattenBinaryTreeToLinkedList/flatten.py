# Method 1: preorder tarversal and then iterate each node
def flatten(self, root):
    preorder = []
    def helper(root):
        if root:
            preorder.append(root)
            helper(root.left)
            helper(root.right)
    helper(root)
    for i in range(len(preorder) - 1):
        preorder[i].left = None
        preorder[i].right = preorder[i + 1]
    
# Method 2: reverse preorder traversal, only one pass
def flatten(self, root):
    self.tail = None
    
    def helper(root):
        if not root: return None
        helper(root.right)
        helper(root.left)
        
        root.left = None
        root.right = self.tail
        self.tail = root
    helper(root)