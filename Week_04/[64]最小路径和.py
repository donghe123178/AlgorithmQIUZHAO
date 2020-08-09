# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。 
# 
#  说明：每次只能向下或者向右移动一步。 
# 
#  示例: 
# 
#  输入:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。
#  
#  Related Topics 数组 动态规划 
#  👍 614 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        """
        动态规划
        1.子问题
        2.dp数组，起始点到[i][j]的最小路径和
        3.dp方程，dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        复杂度分析：
        时间复杂度O(M*N)
        空间复杂度O(M*N)
        """
        # if not grid:
        #     return 0
        # m = len(grid)
        # n = len(grid[0])
        # dp = [[0]*n for _ in range(m)]
        # for i in range(m):
        #     for j in range(n):
        #         if i == 0 and j == 0:
        #             dp[i][j] = grid[i][j]
        #         elif i == 0:
        #             dp[i][j] = grid[i][j] + dp[i][j-1]
        #         elif j == 0:
        #             dp[i][j] = grid[i][j] + dp[i-1][j]
        #         else:
        #             dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        # return dp[m-1][n-1]

        """
        优化：直接修改原矩阵，不使用额外空间
        空间复杂度O(1)
        """
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i==j==0:
                    continue
                elif i == 0:
                    grid[i][j] += grid[i][j-1]
                elif j == 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]
# leetcode submit region end(Prohibit modification and deletion)
