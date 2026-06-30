class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        string = s.split()
        count = len(string[-1])
        return count
s = "Hello world"
object = Solution() 
print(object.lengthOfLastWord(s))
        