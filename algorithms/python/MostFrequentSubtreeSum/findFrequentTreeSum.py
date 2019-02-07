def findFrequentTreeSum(self, root):
    count = {}
    
    def helper(root):
        if not root: return 0
        temp = root.val + helper(root.left) + helper(root.right)
        count[temp] = count.get(temp, 0) + 1
        return temp
    
    helper(root)
    return [key for key, val in count.items() if val == max(count.values())]