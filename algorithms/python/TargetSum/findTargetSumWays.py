def findTargetSumWays(self, nums: List[int], S: int) -> int:
    count = {nums[0]:1, -nums[0]:1} if nums[0] != 0 else {0:2}
    for n in nums[1:]:
        temp = {}
        for val in count:
            temp[val + n] = temp.get(val + n, 0) + count[val]
            temp[val - n] = temp.get(val - n, 0) + count[val]
        count = temp
    return count.get(S, 0)