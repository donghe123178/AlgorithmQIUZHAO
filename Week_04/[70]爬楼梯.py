# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。 
# 
#  每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？ 
# 
#  注意：给定 n 是一个正整数。 
# 
#  示例 1： 
# 
#  输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶 
# 
#  示例 2： 
# 
#  输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶
#  
#  Related Topics 动态规划 
#  👍 1176 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        动态递推，时间复杂度，空间复杂度都是O(N)
        """
        if n <= 2:
            return n
        # 状态空间
        dp = [0] * (n+1)
        # 初始条件
        dp[0], dp[1], dp[2]= 0, 1, 2
        # 递推方程
        for i in range(3, n+1):
            dp[i] = dp[i-2] + dp[i-1]
        return dp[n]

        """
        2.改进,不需要把每一个状态都记录下来
        空间复杂度为常数
        """
        # if n <= 2:
        #     return n
        # re, p, q =0, 1, 2
        # for i in range(3, n + 1):
        #     re = p + q
        #     p, q = q, re
        # return re

        """
        拓展：
        可以走1，2，3步
        相邻两步的步伐不能相同
        打印出方法
        """
    #     steps = [1, 2, 3]
    #     self._dfs(n, [], steps)
    #
    # def _dfs(self, n, res, steps):
    #     # 递归终止条件
    #     if n == 0:
    #         print(res)
    #         return
    #
    #     for step in steps:
    #         if n >= step:
    #             self._dfs(n-step, res + [step], steps)



if __name__ == '__main__':
    a = Solution()
    a.climbStairs(3)

# leetcode submit region end(Prohibit modification and deletion)
