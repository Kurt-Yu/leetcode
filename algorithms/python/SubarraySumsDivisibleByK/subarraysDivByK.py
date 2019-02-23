def subarraysDivByK(self, A: 'List[int]', K: 'int') -> 'int':
    res = 0
    temp = [1] + [0] * K
    prefix = 0
    for a in A:
        prefix = (prefix + a) % K
        res += temp[prefix]
        temp[prefix] += 1
    return res