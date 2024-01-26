"""
https://leetcode.com/problems/out-of-boundary-paths/description/?envType=daily-question&envId=2024-01-26
"""
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp = {}
        def recurse(i, j, moves):
            cache = (i, j, moves)
            if i<0 or j<0 or i>m-1 or j>n-1:
                return 1
            elif moves == 0:
                return 0
            elif cache in dp:
                return dp[cache]
            else:
                direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                total = 0
                for d in direction:
                    di, dj = d
                    total += recurse(i + di, j + dj, moves - 1)
                dp[cache] = total
                print(dp)
                return dp[cache]
        return recurse(startRow, startColumn, maxMove) % (10**9 + 7)
    
print(Solution().findPaths(2,2,2,0,0))