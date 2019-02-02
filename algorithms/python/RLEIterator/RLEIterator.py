class RLEIterator:

    def __init__(self, A):
        self.input = A
        self.count = 0
        for i in range(0, len(A), 2):
            self.count += A[i]
        
    def next(self, n):
        if n > self.count: return -1
        index = 0
        while index < len(self.input):
            if self.input[index] == 0:
                self.input = self.input[index + 2:]
            elif n <= self.input[index]:
                self.input[index] -= n
                return self.input[index + 1]
            else:
                n -= self.input[index]
                self.input = self.input[index + 2:]
        if n > 0: return -1