def findKthLargest(self, nums: List[int], k: int) -> int:
    import random
    random.shuffle(nums)
    
    pivot = nums[0]
    smaller, bigger = [], []
    for n in nums:
        if n < pivot: smaller.append(n)
        if n > pivot: bigger.append(n)
    

    if k <= len(bigger):
        return self.findKthLargest(bigger, k)
    elif k <= len(nums) - len(smaller):
        return pivot
    else:
        return self.findKthLargest(smaller, k - len(nums) + len(smaller))