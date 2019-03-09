def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
    
    return heapq.nsmallest(K, points, lambda x: x[0] * x[0] + x[1] * x[1])