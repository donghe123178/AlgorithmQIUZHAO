# 在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。 
# 
#  示例: 
# 
#  输入: 
# 
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# 
# 输出: 4 
#  Related Topics 动态规划 
#  👍 503 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        """
        动态规划
        dp数组含义：dp[i][j] 是指一个正方形以matrix[i-1][j-1]为右下角的最大边长
        递推方程：
        当matrix[i-1][j-1] == 1时：
        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        取max(dp)
        复杂度分析：
        时间空间复杂度均为O(MN)
        """
        # if not matrix:
        #     return 0
        # m = len(matrix)
        # n = len(matrix[0])
        # dp = [[0]*(n+1) for _ in range(m+1)]
        # max_side = 0
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == "1":
        #             dp[i+1][j+1] = min(dp[i][j+1], dp[i+1][j], dp[i][j]) + 1
        #             max_side = max(max_side, dp[i+1][j+1])
        # return max_side * max_side

        """
        空间优化，降维，想象成一个一维行矩阵从矩阵上滑动下来
        空间复杂度为O(n)
        """
        if not matrix:
            return 0
        n = len(matrix[0])
        dp = [0]*(n+1)
        max_side = 0
        for char in matrix:
            north_west = 0
            for j in range(n):
                # 格子的左，上，斜上方向对比，而斜上方向的值是由上一行产生的
                # 每次循环进入下一列时，要提前取出，不然下面的计算会覆盖掉
                tmp = dp[j+1]
                if char[j] == "1":
                    dp[j+1] = min(dp[j], dp[j+1], north_west) + 1
                    max_side = max(max_side, dp[j+1])
                else:
                    dp[j + 1] = 0
                north_west = tmp
        return max_side * max_side


# leetcode submit region end(Prohibit modification and deletion)
