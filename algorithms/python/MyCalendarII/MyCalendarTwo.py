class MyCalendarTwo(object):

    def __init__(self):
        self.single = []
        self.double = []
        
    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for i, j in self.double:
            if start < j and end > i:
                return False
        for i, j in self.single:
            if start < j and end > i:
                self.double.append((max(start, i), min(end, j)))
        self.single.append((start, end))
        return True