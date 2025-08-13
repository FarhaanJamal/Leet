class Solution(object):
    def numMovesStones(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        x, y, z = sorted([a, b, c])
        ans = [0, 0]
        diff1 = abs(y-x) -1
        if diff1 > 0:
            ans[0] += 1
            ans[1] += diff1
        diff2 = abs(z-y) -1
        if diff2 > 0:
            if diff1 != 1: 
                ans[0] += 1
            if diff2 == 1:
                ans[0] = 1
            ans[1] += diff2
        return ans
        