def leastInterval(self, tasks: 'List[str]', n: 'int') -> 'int':
    val = list(collections.Counter(tasks).values())
    largest = max(val)
    count = val.count(largest)
    return max(len(tasks), (largest - 1) * (n + 1) + count)