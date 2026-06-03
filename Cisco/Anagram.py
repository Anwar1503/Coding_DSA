##https://leetcode.com/problems/valid-anagram/


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        freq_char = {}
        for i in s:
            freq_char[i] = freq_char.get(i,0) + 1
        for i in t:
            freq_char[i] = freq_char.get(i,0) - 1
        
        for value in freq_char.values():
            if(value) != 0:
                return False
        return True        

        