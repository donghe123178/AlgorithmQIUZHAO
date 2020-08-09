# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。 
# 
#  相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。 
# 
#  
# 
#  例如，给定三角形： 
# 
#  [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
#  
# 
#  自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。 
# 
#  
# 
#  说明： 
# 
#  如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。 
#  Related Topics 数组 动态规划 
#  👍 557 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        """
        DP步骤：
        1.重复性，problem(i,j) = min(sub(i+1, j) +sub(i+1, j+1)) + a[i+j]
        2.状态数组,dp[i][j]存储每个子问题的最小路径和
        3.状态转移过程dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + a[i+j]
        """
        # 1.自顶向下
        # 空间复杂度o(n*n/2)
        # if not triangle:
        #     return
        # dp = [[0] * len(row) for row in triangle]
        # dp[0][0] = triangle[0][0]
        # for i in range(1, len(triangle)):
        #     for j in range(len(triangle[i])):
        #         if j == 0:
        #             dp[i][j] = dp[i - 1][j] + triangle[i][j]
        #         elif j == len(triangle[i]) - 1:
        #             dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
        #         else:
        #             dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]
        # return min(dp[-1])

        # 自顶向下，复用空间
        # if not triangle:
        #     return
        # for i in range(1, len(triangle)):
        #     for j in range(len(triangle[i])):
        #         if j == 0:
        #             triangle[i][j] += triangle[i - 1][j]
        #         elif j == len(triangle[i]) - 1:
        #             triangle[i][j] += triangle[i - 1][j - 1]
        #         else:
        #             triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j])
        # return min(triangle[-1])

        # 自底向上，O(N)的空间复杂度
        if not triangle:
            return
        dp = triangle[-1]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = min(dp[j+1], dp[j]) + triangle[i][j]
        return dp[0]

        # 自底向上，复用空间
        # if not triangle:
        #     return
        # for i in range(len(triangle)-2, -1, -1):
        #     for j in range(len(triangle[i])):
        #         triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        # return triangle[0][0]
# leetcode submit region end(Prohibit modification and deletion)
