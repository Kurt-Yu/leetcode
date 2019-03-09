def maximumSwap(self, num: int) -> int:
    num = list(str(num))
    temp = sorted([int(n) for n in num])
    i, j = 0, len(temp) - 1
    
    while i < len(num) and j >= 0:
        if int(num[i]) == temp[j]:
            i, j = i + 1, j - 1
        elif int(num[i]) < temp[j]:
            for k in range(len(num) - 1, -1, -1):
                if int(num[k]) == temp[j]:
                    num[k], num[i] = num[i], num[k]
                    return int(''.join(num))
    return int(''.join(num))