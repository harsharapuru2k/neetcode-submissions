class Solution:
    def reorganizeString(self, s: str) -> str:
        

        count=Counter(s)

        heap=[[-val,key] for key,val in count.items()]
        heapq.heapify(heap)

        q=deque()
        s=""
        count=0
        
        while heap or q:
            
            if heap:
                x=heapq.heappop(heap)
                s+=x[1]

            if len(s)>1 and s[-1]==s[-2]:
                return ""

            if q:
                heapq.heappush(heap,q.popleft())
            
            if x[0]<-1:
                q.append([x[0]+1,x[1]])
            
            
        return s