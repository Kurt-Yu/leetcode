def constructMaximumBinaryTree(self, nums):
    if not nums: return None
    index = nums.index(max(nums))
    root = TreeNode(nums[index])
    root.left = self.constructMaximumBinaryTree(nums[:index])
    root.right = self.constructMaximumBinaryTree(nums[index + 1:])
    return root
    