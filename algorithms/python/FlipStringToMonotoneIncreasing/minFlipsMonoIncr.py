def minFlipsMonoIncr(self, S):
    n = len(S)
    count0 = S.count('0')
    res = n - count0
    count1 = 0
    for s in S:
        if s == '0':
            count0 -= 1
        else:
            res = min(res, count0 + count1)
            count1 += 1
    return res