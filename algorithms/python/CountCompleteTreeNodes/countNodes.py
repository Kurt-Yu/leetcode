# Method 1:
def countNodes(self, root):
    if not root: return 0
    hl, hr = 0, 0
    l, r = root, root
    while l:
        hl += 1
        l = l.left
    while r:
        hr += 1
        r = r.right
    if hl == hr: return pow(2, hl) - 1
    return 1 + self.countNodes(root.left) + self.countNodes(root.right)

# Method 2:
def countNodes(self, root):
    if not root: return 0
    return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    

# Method 3: O(logn ^ 2) solution
def countNodes(self, root):
    if not root: return 0
    left, right = self.height(root.left), self.height(root.right)
    if left == right:
        return pow(2, left) + self.countNodes(root.right)
    else:
        return pow(2, right) + self.countNodes(root.left)
        
def height(self, root):
    if not root: return 0
    return 1 + self.height(root.left)