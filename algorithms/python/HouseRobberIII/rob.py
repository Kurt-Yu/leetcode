"""
Answe inspired by the post from here: 
https://leetcode.com/problems/house-robber-iii/discuss/79330/Step-by-step-tackling-of-the-problem
"""

# Method 1: naive recursive solution: O(2 ^ n), exponential time
def rob(self, root):
    if not root: return 0
    val = 0
    if root.left:
        val += self.rob(root.left.left) + self.rob(root.left.right)
    if root.right:
        val += self.rob(root.right.left) + self.rob(root.right.right)

    return max(val + root.val, self.rob(root.left) + self.rob(root.right))

# Method 2: recursive with memorization
def rob(self, root):
    memo = {}

    def helper(root):
        if not root: return 0
        if root in memo: return memo[root]

        val = 0
        if root.left:
            val += helper(root.left.left) + helper(root.left.right)
        if root.right:
            val += helper(root.right.left) + helper(root.right.right)

        val = max(root.val + val, helper(root.left) + helper(root.right))
        memo[root] = val
        return val
    return helper(root)

# Method 3: greedy approach
def helper(root):
    if not root: return [0, 0]
    left = helper(root.left)
    right = helper(root.right)
    temp = [max(left[0], left[1]) + max(right[0], right[1]), root.val + left[0] + right[0]]
    return temp
return max(helper(root))