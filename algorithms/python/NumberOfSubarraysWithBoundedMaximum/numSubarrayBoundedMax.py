def numSubarrayBoundedMax(self, A: 'List[int]', L: 'int', R: 'int') -> 'int':
    res, j, count = 0, 0, 0
    for i in range(len(A)):
        if L <= A[i] <= R:
            res += i - j + 1
            count = i - j + 1
        elif A[i] < L:
            res += count
        else:
            j = i + 1
            count = 0
    return res