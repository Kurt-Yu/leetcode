# Method 1: bfs and choose the last node of each level
def rightSideView(self, root: 'TreeNode') -> 'List[int]':
    if not root: return []
    stack = [root]
    res = []
    while stack:
        res.append(stack[-1].val)
        stack = [child for node in stack for child in (node.left, node.right) if child]
    return res

# Recursive soliution
# The idea is that for each level, we only choose one node
# And if the result list length is the same as depth, we add this node
def rightSideView(self, root: 'TreeNode') -> 'List[int]':
    res = []
    def helper(root, depth):
        if not root: return
        if len(res) == depth:
            res.append(root.val)
        helper(root.right, depth + 1)
        helper(root.left, depth + 1)
    helper(root, 0)
    return res