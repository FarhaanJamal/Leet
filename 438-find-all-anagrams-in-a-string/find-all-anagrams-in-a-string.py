class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_sort = sorted(p)
        ans = []
        ln = len(p)
        for r in range(ln-1, len(s)):
            window = sorted(s[r-ln+1:r+1])
            if p_sort == window:
                ans.append(r-ln+1)
        return ans


            

