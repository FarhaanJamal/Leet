class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        ln = len(height)
        l_max, r_max = [0]*ln, [0]*ln
        l_max[0] = height[0]
        r_max[ln-1] = height[ln-1]
        for i in range(1, ln):
            l_max[i] = max(l_max[i-1], height[i])
        for i in range(ln-2, -1, -1):
            r_max[i] = max(r_max[i+1], height[i])
        for i in range(ln):
            ans += min(l_max[i], r_max[i]) - height[i]
        return ans