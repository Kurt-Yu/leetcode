def tree2str(self, root):
    if not root:
        return ''
    if root.left and root.right:
        return '{0}({1})({2})'.format(root.val, self.tree2str(root.left), self.tree2str(root.right))
    elif not root.left and root.right:
        return '{0}()({1})'.format(root.val, self.tree2str(root.right))
    elif root.left and not root.right:
        return '{0}({1})'.format(root.val, self.tree2str(root.left))
    else:
        return str(root.val)