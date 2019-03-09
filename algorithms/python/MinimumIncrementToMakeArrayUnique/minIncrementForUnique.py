def minIncrementForUnique(self, A: 'List[int]') -> 'int':
    res = need = 0
    for a in sorted(A):
        res += max(need - a, 0)
        need = max(need + 1, a + 1)
    return resw