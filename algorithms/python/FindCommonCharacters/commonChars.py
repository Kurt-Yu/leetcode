# Stupid Way:
def commonChars(self, A: List[str]) -> List[str]:
    count = [collections.Counter(word) for word in A]
    compare = count[0]
    res = []
    for k, v in compare.items():
        val = v
        flag = True
        for c in count[1:]:
            if k not in c: 
                flag = False
                break
            val = min(val, c[k])
        if flag:
            for i in range(val):
                res.append(k)
    return res

# pythonic way:
def commonChars(self, A: List[str]) -> List[str]:
    res = collections.Counter(A[0])
    for a in A:
        res &= collections.Counter(a)
    return list(res.elements())