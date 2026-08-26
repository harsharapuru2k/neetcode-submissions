class Solution:

    def backtrack(self,idx,cs):

        self.result.append(cs[:])

        for i in range(idx,len(self.nums)):
            
            cs.append(self.nums[i])

            self.backtrack(i+1,cs)

            cs.pop()
        
        return

    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        self.result=[]
        self.nums=nums

        self.backtrack(0,[])

        return self.result