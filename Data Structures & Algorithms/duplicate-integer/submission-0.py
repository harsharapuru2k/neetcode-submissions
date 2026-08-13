class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        s=set()

        for element in nums:
            if element in s:
                return True
            s.add(element)
        
        return False
        