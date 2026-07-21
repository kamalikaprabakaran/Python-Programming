class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pointer  = 0
        t_pointer = 0
        if len(s) == 0:
            return True
        else:
            while t_pointer < len(t):
                if s[s_pointer] != t[t_pointer]:
                    t_pointer+=1
                else:
                    s_pointer+=1
                    t_pointer+=1
                    if s_pointer == len(s):
                        return True
        return False
obj = Solution()
print(obj.isSubsequence("abs","ahbgdc"))