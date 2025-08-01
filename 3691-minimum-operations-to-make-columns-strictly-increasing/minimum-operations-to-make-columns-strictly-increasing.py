class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        ln = len(grid)
        if ln == 1:
            return 0
        ans = 0
        for i in range(1, ln):
            for j in range(len(grid[0])):
                curr, prev = grid[i][j], grid[i-1][j]
                if curr > prev:
                    continue
                temp = prev - curr + 1
                grid[i][j] += temp
                ans += temp
                print(i, j, temp, ans)
        return ans