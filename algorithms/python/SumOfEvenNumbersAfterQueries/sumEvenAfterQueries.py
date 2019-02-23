def sumEvenAfterQueries(self, A, queries):
    res = []
    even = sum(a for a in A if a % 2 == 0)
    for val, index in queries:
        if A[index] % 2 == 0:
            if val % 2 == 0: even += val
            else: even -= A[index]
        else:
            if val % 2 != 0: even += val + A[index]
        res.append(even)
        A[index] += val
    return res