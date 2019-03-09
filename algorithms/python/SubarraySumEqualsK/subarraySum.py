def subarraySum(self, nums: 'List[int]', k: 'int') -> 'int':
    res = 0
    prefix = {0:1}
    total = 0
    for n in nums:
        total += n
        if total - k in prefix:
            res += prefix[total - k]
        prefix[total] = prefix.get(total, 0) + 1
    return res