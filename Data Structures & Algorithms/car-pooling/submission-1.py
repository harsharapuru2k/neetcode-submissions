class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:


        heap=[]

        for li in trips:
            heapq.heappush(heap,[li[1],li[2],li[0]])
        
        kms=0
        cc=0
        heap2=[]

        while heap:
            if heap:
                kms=heap[0][0]

            while heap2 and  heap2[0][0]<=kms:
                y=heapq.heappop(heap2)
                cc-=y[1]

            while heap and heap[0][0]<=kms:
                x=heapq.heappop(heap)
                cc+=x[2]
                heapq.heappush(heap2,[x[1],x[2]])
                if cc>capacity:
                    return False
    
        return True



        