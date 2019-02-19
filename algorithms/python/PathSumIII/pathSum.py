# Method 1:
# time complexity: O(n)
# space complexity: O(n)
def pathSum(self, root, target):
    self.result = 0
    cache = {0:1}
    
    def dfs(root, currPathSum):
        if not root: return  

        currPathSum += root.val
        oldPathSum = currPathSum - target

        self.result += cache.get(oldPathSum, 0)
        cache[currPathSum] = cache.get(currPathSum, 0) + 1


        dfs(root.left, currPathSum)
        dfs(root.right, currPathSum)

        cache[currPathSum] -= 1
    
    dfs(root, 0)
    return self.result

# Method 2:
# Using two dfs calls, first dfs traversal every node in the tree
# second dfs: for every node, check if every paths of this node sums up to target
# Time complexity: O(nlogn) - O(n^2)
# Spaec complexity: O(1)
def pathSum(self, root, total):
    self.res = 0
    def test(root, target):
        if root:
            if root.val == target: self.res += 1
            test(root.left, target - root.val)
            test(root.right, target - root.val)
    
    
    def dfs(root):
        if root:
            test(root, total)
            dfs(root.left)
            dfs(root.right)
    
    dfs(root)
    return self.res