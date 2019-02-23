# Method 1: binary search with recursion:
def findPeakElement(self, nums: 'List[int]') -> 'int':
    def helper(low, high):
        if low == high: return low
        mid = (low + high) // 2
        if nums[mid] > nums[mid + 1]:
            return helper(low, mid)
        else:
            return helper(mid + 1, high)
        
    return helper(0, len(nums) - 1)
    
# Method 2: binary search iterative solution:
def findPeakElement(self, nums: 'List[int]') -> 'int':
    low, high = 0, len(nums) - 1
    while low < high:
        mid = (low + high) // 2
        if nums[mid] < nums[mid + 1]:
            low = mid + 1
        else:
            high = mid
    return low