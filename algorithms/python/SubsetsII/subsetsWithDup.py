def subsetsWithDup(self, nums: 'List[int]') -> 'List[List[int]]':
    res = []
    nums.sort()
    def backtracking(temp, start):
        res.append(temp[:])
        for i in range(start, len(nums)):
            if i != start and nums[i] == nums[i - 1]: continue
            temp.append(nums[i])
            backtracking(temp, i + 1)
            temp.pop()
    backtracking([], 0)
    return res