class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balls = dict()
        colors = dict()
        ans = []
        for [ball, color] in queries:
            if ball in balls:
                if balls[ball] in colors:
                    if colors[balls[ball]] > 1:
                        colors[balls[ball]] -= 1
                    else:
                        del colors[balls[ball]]

            balls[ball] = color
            if color in colors:
                colors[color] += 1
            else:
                colors[color] = 1
            ans.append(len(colors))
        
        return ans
        