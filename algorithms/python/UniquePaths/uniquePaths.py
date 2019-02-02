def uniquePaths(self, m, n):
    count = m + n - 2
    choose = n - 1
    a = b = 1
    for _ in range(n - 1):
        a *= count
        count -= 1
        b *= choose
        choose -= 1
    return int(a / b)