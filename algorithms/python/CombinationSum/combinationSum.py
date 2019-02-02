def combinationSum(self, candidates, target):
    res = []
    candidates.sort()
    
    def backtracking(temp, remaining, start):
        if remaining < 0: return
        if remaining == 0: res.append(temp[:])
        for i in range(start, len(candidates)):
            temp.append(candidates[i])
            backtracking(temp, remaining - candidates[i], i)
            temp.pop()
    
    backtracking([], target, 0)
    return res
