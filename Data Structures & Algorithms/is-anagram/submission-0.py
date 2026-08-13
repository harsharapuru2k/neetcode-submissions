class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False

        dict_s={}

        for element in s:
            dict_s[element]=dict_s.get(element,0)+1
        
        for element in t:
            if element in dict_s:
                dict_s[element]-=1
            else:
                return False
        
        for index in dict_s:
            if dict_s[index]!=0:
                return False
        
        return True
        