def addToArrayForm(self, A, K):
    a = 0
    for i in A:
        a = a * 10 + i
    
    a += K
    
    return [int(i) for i in str(a)]