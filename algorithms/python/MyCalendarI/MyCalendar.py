# Method 1: using heapq, time complexity: O(n)
# where n is the current number of self.bookings
import heapq

class MyCalendar:
    def __init__(self):
        self.booking = []
        
    def book(self, start, end):
        for a, b in self.booking:
            if not (end <= a or b <= start):
                return False
        heapq.heappush(self.booking, (start, end))
        return True

# Method 2: binary search tree
class Node:
    def __init__(self,s,e):
        self.e = e
        self.s = s
        self.left = None
        self.right = None


class MyCalendar(object):

    def __init__(self):
        self.root = None

    def book_helper(self,s,e,node):
        if s>=node.e:
            if node.right:
                return self.book_helper(s,e,node.right)
            else:
                node.right = Node(s,e)
                return True
        elif e<=node.s:
            if node.left:
                return self.book_helper(s,e,node.left)
            else:
                node.left = Node(s,e)
                return True
        else:
            return False
        
    def book(self, start, end):
        if not self.root:
            self.root = Node(start,end)
            return True
        return self.book_helper(start,end,self.root)