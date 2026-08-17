class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        length=min(len(word1),len(word2))
        s=""

        i=0
        while i<length:
            s+=word1[i]+word2[i]
            i+=1
        
        while i<len(word1):
            s+=word1[i]
            i+=1
        
        while i<len(word2):
            s+=word2[i]
            i+=1
        
        return s
            
