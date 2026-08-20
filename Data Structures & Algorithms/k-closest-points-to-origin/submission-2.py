class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        result=[]
        heap=[]
        for co in points:
            x,y=[co[0],co[1]]
            heapq.heappush(heap,(x**2+y**2,[x,y]))
        
        i=k
        while heap and i>0:
            result.append(heapq.heappop(heap)[1])
            i-=1

        
        return result