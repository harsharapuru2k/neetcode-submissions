class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap=[]

        i=1
        for num in nums:
            heapq.heappush(heap,num)

            if i>k:
                heapq.heappop(heap)
            i+=1
        
        return heap[0]
        