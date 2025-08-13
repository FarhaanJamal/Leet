class Solution(object):
    def numMovesStones(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        """x, y, z = sorted([a, b, c])
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
        return ans"""
        x, y, z = sorted([a, b, c])
        min_move, max_move = 0, 0
        if y-x == 1 and z-y == 1:
            min_move = 0
        elif y-x > 2 and z-y > 2:
            min_move = 2
        else:
            min_move = 1
        max_move = (y-x) + (z-y) - 2 
        return [min_move, max_move]
        