class CBTInserter:

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.tree = []
        if not root: self.tree = []
        else:
            stack = [root]
            while stack:
                node = stack.pop(0)
                self.tree.append(node)
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)

    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        node = TreeNode(v)
        self.tree.append(node)
        parent = self.tree[len(self.tree) // 2 - 1]
        if len(self.tree) % 2 == 0: parent.left = node
        else: parent.right = node
        return parent.val
        

    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.tree[0]