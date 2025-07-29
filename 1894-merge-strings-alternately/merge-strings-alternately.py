class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pnt1, pnt2 = 0, 0
        ans = ""
        while len(word1) > pnt1 or len(word2) > pnt2:
            if len(word1) > pnt1:
                ans += word1[pnt1]
            if len(word2) > pnt2:
                ans += word2[pnt2]
            pnt1 += 1
            pnt2 += 1
        return ans
        