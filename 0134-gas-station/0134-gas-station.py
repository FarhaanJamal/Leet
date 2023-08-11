class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) >= sum(cost):
            ans, tot = 0, 0
            for i in range(len(gas)):
                tot += gas[i] - cost[i]
                if tot < 0:
                    ans = i+1
                    tot = 0
            return ans
        return -1