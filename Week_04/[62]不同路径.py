# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。 
# 
#  机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。 
# 
#  问总共有多少条不同的路径？ 
# 
#  
# 
#  例如，上图是一个7 x 3 的网格。有多少可能的路径？ 
# 
#  
# 
#  示例 1: 
# 
#  输入: m = 3, n = 2
# 输出: 3
# 解释:
# 从左上角开始，总共有 3 条路径可以到达右下角。
# 1. 向右 -> 向右 -> 向下
# 2. 向右 -> 向下 -> 向右
# 3. 向下 -> 向右 -> 向右
#  
# 
#  示例 2: 
# 
#  输入: m = 7, n = 3
# 输出: 28 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= m, n <= 100 
#  题目数据保证答案小于等于 2 * 10 ^ 9 
#  
#  Related Topics 数组 动态规划 
#  👍 630 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        """
        1.动态规划，递推，思维是自底向上
        时间复杂度O(M*N)
        空间复杂度O(M*N)
        """
        # 生成一个二维数组m行n列
        # dp = [[0 for col in range(n)] for row in range(m)]
        # for i in range(n):
        #     dp[0][i] = 1
        # for i in range(m):
        #     dp[i][0] = 1
        # for i in range(1, m):
        #     for j in range(1, n):
        #         dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # return dp[-1][-1]
        """
        优化，空间复杂度降为一维,杨辉三角形，每个位置得路径=该位置左边得路径+该位置上边的路径
        时间复杂度O(M*N)
        空间复杂度O(N)
        """
        cur = [1]*n
        for i in range(1,m):
            for j in range(1,n):
                cur[j] += cur[j-1]
        return cur[-1]

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    dp = [[0 for col in range(3)] for row in range(2)]
    print(dp)