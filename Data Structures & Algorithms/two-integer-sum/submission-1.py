class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d={}

        for ele in range(len(nums)):
            if nums[ele] in d:
                return [d[nums[ele]],ele]
            else:
                d[target-nums[ele]]=ele
            
