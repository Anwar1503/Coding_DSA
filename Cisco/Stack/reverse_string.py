##https://leetcode.com/problems/reverse-string/

##two pointers
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i=0
        j=len(s) - 1
        while(i<j):
            s[i],s[j] = s[j],s[i]
            i += 1
            j -= 1 

##stack            

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        stack = []
        midString = ""
        for char in s:
            stack.append(s)
        while stack:
            reversed_string += stack.pop() 