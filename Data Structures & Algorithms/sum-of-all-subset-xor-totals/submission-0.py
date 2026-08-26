class Solution:

    def backtrack(self,idx,cs):

        if cs:
        
            res=0
            for num in cs:
                res^=num

            self.result.append(res)

        for i in range(idx,len(self.nums)):
            
            cs.append(self.nums[i])

            self.backtrack(i+1,cs)

            cs.pop()
        
        return


    def subsetXORSum(self, nums: List[int]) -> int:
        self.result=[]
        self.nums=nums

        self.backtrack(0,[])

        return sum(self.result)

        
        