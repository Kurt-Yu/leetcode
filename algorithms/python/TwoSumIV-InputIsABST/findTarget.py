# Method 1: inorder tarversal

def findTarget(self, root, k):
    inorder = []
    
    def helper(root):
        if root:
            helper(root.left)
            inorder.append(root.val)
            helper(root.right)
    
    helper(root)
    
    d = set()
    for num in inorder:
        if k - num in d:
            return True
        else:
            d.add(num)
    return False

# Method 2: inorder traversal using one pass
def findTarget(self, root, k):
    if not root: return False
    dfs, s = [root], set()
    for node in dfs:
        if k - node.val in s: return True
        s.add(node.val)
        if node.left: dfs.append(node.left)
        if node.right: dfs.append(node.right)
    return False