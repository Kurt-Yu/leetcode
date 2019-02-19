"""
Method 1: naive solution: tarverse the tree and find the second smallest in the list
"""
def findSecondMinimumValue(self, root):
    s = set()
    def helper(root):
        if root:
            s.add(root.val)
            helper(root.left)
            helper(root.right)
    helper(root)
    if len(s) == 1 or len(s) == 0: return -1
    s.remove(min(s))
    return min(s)
    

"""
Method 2: this problem is basically ask for the smallest value in subtrees,
so we can just use a variable `self.res` to track that value
update it when encounter a smaller value
"""
def findSecondMinimumValue(self, root):
    self.res = float('inf')
    def helper(node):
        if node:
            if root.val< node.val < self.res:
                self.res = node.val
            helper(node.left)
            helper(node.right)
    helper(root)
    return self.res if self.res != float('inf') else -1



"""
Method 3:

because of the special porperty of the tree, the question basically is asking to find
the smallest element in the subtree of root. So, we can recursively find left and right
value that is not equal to the root's value, and then return the smaller one of them
"""
def findSecondMinimumValue(self, root):
    if not root: return -1
    if not root.left and not root.right: return -1
    
    left, right = root.left.val, root.right.val
    if left == root.val: left = self.findSecondMinimumValue(root.left)
    if right == root.val: right = self.findSecondMinimumValue(root.right)
    if left != -1 and right != -1: return min(left, right)
    if left == -1: return right
    if right == -1: return left