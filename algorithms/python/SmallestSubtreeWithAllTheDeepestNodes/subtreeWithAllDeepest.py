# Method 1: one pass, time complexty: O(n)

def subtreeWithAllDeepest(self, root):
    def helper(root):
        if not root: return 0, None
        l, r = helper(root.left), helper(root.right)
        if l[0] > r[0]: return l[0] + 1, l[1]
        elif l[0] < r[0]: return r[0] + 1, r[1]
        else: return l[0] + 1, root
    return helper(root)[1]

# Method 2: more striaght forward but more time comsuming, exponential time
class Solution:
    def subtreeWithAllDeepest(self, root):
        if not root: return None
        if self.height(root.left) == self.height(root.right):
            return root
        elif self.height(root.left) > self.height(root.right):
            return self.subtreeWithAllDeepest(root.left)
        else:
            return self.subtreeWithAllDeepest(root.right)
        
    def height(self, root):
            if not root: return 0
            return 1 + max(self.height(root.left), self.height(root.right))