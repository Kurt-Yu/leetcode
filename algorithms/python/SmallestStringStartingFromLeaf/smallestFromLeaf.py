def smallestFromLeaf(self, root: 'TreeNode') -> 'str':
    if not root: return ''
    left = self.smallestFromLeaf(root.left)
    right = self.smallestFromLeaf(root.right)
    return (left if right == '' or (left != '' and left < right) else right) + chr(97 + root.val)