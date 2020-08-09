# 写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项。斐波那契数列的定义如下： 
# 
#  F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), 其中 N > 1. 
# 
#  斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。 
# 
#  答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 2
# 输出：1
#  
# 
#  示例 2： 
# 
#  输入：n = 5
# 输出：5
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= n <= 100 
#  
# 
#  注意：本题与主站 509 题相同：https://leetcode-cn.com/problems/fibonacci-number/ 
#  Related Topics 递归 
#  👍 44 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        1.递归，指数级，时间复杂度为O(2^N)
        带一个备忘录，时间复杂度为O(n),空间复杂度O(N)
        自顶向下
        """
        #     if n < 1:
        #         return 0
        #     li = [0] * (n + 1)
        #     return self.helper(n,li)
        #
        # def helper(self,n,li):
        #     # 基本情况
        #     if n == 1 or n == 2:
        #         return 1
        #     # 已经计算过
        #     if li[n] != 0:
        #         return li[n]
        #     li[n] = self.helper(n-1, li) d+ self.helper(n-2, li)
        #     return li[n] % 1000000007

        """
        2.动态规划，自底向上
        DP，时间复杂度为O(n),空间复杂度O(N)
        """
        # if n == 1 or n == 2:
        #     return 1
        # dp = [0] * (n+1)
        # dp[1] = dp[2] = 1
        # for i in range(3, n+1):
        #     dp[i] = dp[i-1] + dp[i-2]
        # return dp[n] % 1000000007

        """
        优化：根据斐波那契数列的状态转移方程，当前状态只和之前的两个状态有关，
        并不需要那么长的一个 DP table 来存储所有的状态，只要想办法存储之前的两个状态就行了
        空间复杂度为O(1)
        状态压缩
        """
        if n <= 1:
            return n
        res, p, q = 0, 0, 1
        for i in range(2, n + 1):
            res = p + q
            p, q = q, res
        return res % 1000000007

# leetcode submit region end(Prohibit modification and deletion)
