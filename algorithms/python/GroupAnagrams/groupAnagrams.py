# Method 1: brute force
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    if not strs: return []
    res = collections.defaultdict(list)
    for s in strs:
        temp = str(sorted(s))
        res[temp].append(s)
    return list(res.values())

# Method 2: a better way, without sort, using prime number
# Time complexity: O(n)
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]
    res = collections.defaultdict(list)
    for s in strs:
        key = 1
        for l in s:
            key = key * prime[ord(l) - 97]
        res[key].append(s)
    return list(res.values())