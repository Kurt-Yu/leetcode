def partitionDisjoint(self, A: 'List[int]') -> 'int':
    localMax = A[0]
    m = localMax
    index = 0
    for i in range(1, len(A)):
        if localMax > A[i]:
            localMax, index = m, i
        else:
            m = max(m, A[i])
    return index + 1