"""
Postorder traversal iterative:

Using two stacks, first push root to the first stack,
do the following when the first stack is not empty:
    pop the last node of first stack, push it to second stack
    push all the children nodes to the first stack
    Then print the contents in second stack use reversed order
"""


def postorder(self, root):
    first = [root]
    second = []
    while first:
        node = first.pop()
        if node:
            first += node.children
            second.append(node.val)
    second.reverse()
    return second

"""
Method 2: recursive solution:
"""
def postorder(self, root):
    postorder = []
    
    def helper(root):
        if root:
            for node in root.children:
                helper(node)
            postorder.append(root.val)
    
    helper(root)
    return postorder