def verticalTraversal(self, root):
    if not root: return []
    temp = []
    def helper(root, x, y):
        if root:
            temp.append((x, y, root.val))
            helper(root.left, x - 1, y - 1)
            helper(root.right, x + 1, y - 1)
    helper(root, 0, 0)
    
    def cmp_(a, b):
        if a[0] != b[0]: return a[0] - b[0]
        if a[1] != b[1]: return b[1] - a[1]
        return a[2] - b[2]
    
    temp = sorted(temp, cmp = cmp_)
    res = [[temp[0][2]]]
    for i in range(1, len(temp)):
        if temp[i][0] == temp[i - 1][0]:
            res[-1].append(temp[i][2])
        else:
            res.append([temp[i][2]])
        
    return res