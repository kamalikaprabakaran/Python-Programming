class Solution:
    def reverseString(self, s: list[str]) -> None:
        s = list(s[::-1])
        return s
s = "hello"
object = Solution()
print(object.reverseString(s))
    
        