class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_len= min(len(word1),len(word2))
        merge = ""
        for i in range(min_len):
            merge +=word1[i]
            merge +=word2[i]
        merge+=word1[min_len:]
        merge+=word2[min_len:]
        return merge


                