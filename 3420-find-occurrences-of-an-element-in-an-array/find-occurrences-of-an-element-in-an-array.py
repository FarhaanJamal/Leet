class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        freq = dict()
        cnt = 1
        for ind, val in enumerate(nums):
            if val == x:
                freq[cnt] = ind
                cnt += 1
        ans = []
        for query in queries:
            if query in freq:
                ans.append(freq[query])
            else:
                ans.append(-1)
        return ans