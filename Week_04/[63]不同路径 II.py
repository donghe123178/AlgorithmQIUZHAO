# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。 
# 
#  机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。 
# 
#  现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？ 
# 
#  
# 
#  网格中的障碍物和空位置分别用 1 和 0 来表示。 
# 
#  说明：m 和 n 的值均不超过 100。 
# 
#  示例 1: 
# 
#  输入:
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# 输出: 2
# 解释:
# 3x3 网格的正中间有一个障碍物。
# 从左上角到右下角一共有 2 条不同的路径：
# 1. 向右 -> 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右 -> 向右
#  
#  Related Topics 数组 动态规划 
#  👍 389 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        """
        动态规划
        1.障碍处理
        有障碍 = 此路不通 = 此格没有路线 = 此格路线数为0
        由于初始化每一格路线数 = 0，
        所以遇到障碍格，不更新该格即可。
        2.边界处理
        上面没格子，就只看左边
        左边没格子，就只看上面
        3.循环是从上到下、从左到右的，保证每次当前格的左边、上面的格子已经更新过
        """
        # m, n = len(obstacleGrid), len(obstacleGrid[0])
        # temp = [[0 for j in range(n)] for i in range(m)]
        # for i in range(m):
        #     if obstacleGrid[i][0] == 0:
        #         temp[i][0] = 1
        #     else:
        #         break
        # for j in range(n):
        #     if obstacleGrid[0][j] == 0:
        #         temp[0][j] = 1
        #     else:
        #         break
        # for i in range(1, m):
        #     for j in range(1, n):
        #         if obstacleGrid[i][j] == 0:
        #             temp[i][j] = temp[i-1][j] + temp[i][j-1]
        # return temp[-1][-1]

        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1
        else:
            return 0
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    continue
                if i > 0:
                    dp[i][j] += dp[i - 1][j]
                if j > 0:
                    dp[i][j] += dp[i][j - 1]
        return dp[-1][-1]

# leetcode submit region end(Prohibit modification and deletion)
