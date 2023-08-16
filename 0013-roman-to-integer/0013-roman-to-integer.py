class Solution:
    def romanToInt(self, s: str) -> int:
        roman_nums = {"I": 1, "V": 5,"X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        ans = 0
        for i in range(len(s)):
            curr_num = roman_nums[s[i]]
            if i+1 < len(s):
                nxt_num = roman_nums[s[i+1]]
            else:
                nxt_num = None
            
            if nxt_num is not None and curr_num < nxt_num:
                ans -= curr_num
            else:
                ans += curr_num
        return ans