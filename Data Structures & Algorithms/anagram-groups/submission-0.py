class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        strs_sorted = ["".join(sorted(word)) for word in strs]
        d={}
        for i in range(len(strs)):
            if strs_sorted[i] in d:
                d[strs_sorted[i]].append(strs[i])
            else:
                d[strs_sorted[i]]=[strs[i]]
        
        result=[]

        for key in d:
            result.append(d[key])
        
        return result