class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pnt1, pnt2 = 0, 0
        ans = ""
        length1 = len(word1)
        length2 = len(word2)
        while length1 > pnt1 or length2 > pnt2:
            if length1 > pnt1:
                ans += word1[pnt1]
            if length2 > pnt2:
                ans += word2[pnt2]
            pnt1 += 1
            pnt2 += 1
        return ans
        