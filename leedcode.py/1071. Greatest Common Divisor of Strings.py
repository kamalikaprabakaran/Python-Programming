class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        small = str1 if len(str1) < len(str2) else str2
        for i in range(len(small),0,-1):
            candidate = small[:i]
            
            if len(str1) % len(candidate) != 0:
                continue
            if len(str2) % len(candidate) !=0:
                continue
            if candidate * (len(str1) // len(candidate)) == str1 and candidate * (len(str2) // len(candidate)) == str2:
                return candidate
        return ""
            
str1="ABABAB"
str2 = "ABC"
object = Solution()
print(object.gcdOfStrings(str1, str2))

            







        