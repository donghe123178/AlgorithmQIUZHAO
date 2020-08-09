# 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回
#  -1。 
# 
#  
# 
#  示例 1: 
# 
#  输入: coins = [1, 2, 5], amount = 11
# 输出: 3 
# 解释: 11 = 5 + 5 + 1 
# 
#  示例 2: 
# 
#  输入: coins = [2], amount = 3
# 输出: -1 
# 
#  
# 
#  说明: 
# 你可以认为每种硬币的数量是无限的。 
#  Related Topics 动态规划 
#  👍 729 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        """
        1.暴力法，递归，指数级
        2.BFS,数的深度就是硬币数
        3.DP：
        子问题，base case ，目标金额为0时返回0
        状态数组，确定状态和选择，
            状态就是原问题和子问题中会变化的变量，目标金额，会不断地向base case靠近
            选择，就是导致状态产生变化的行为
        DP方程的含义：输入一个目标金额n，返回凑出目标金额的最少硬币数量
        状态方程组
        """
        # 分析：子问题总数等于递归数节点个数，每个子问题中含有一个for循环，复杂度为O(K)
        # 总之是指数级别的
        # def dp(n):
        #     # base case
        #     if n == 0: return 0
        #     if n < 0: return -1
        #     # 求最小值，初始化为正无穷
        #     res = float('INF')
        #     for coin in coins:
        #         subproblem = dp(n - coin)
        #         if subproblem == -1: continue
        #         res = min(res, 1 + subproblem)
        #     return res if res != float('INF') else -1
        # return dp(amount)

        # 2.带备忘录的递归,使得子问题总数不会超过金额数
        # 时间复杂度为O(KN)
        # memo = dict()
        #
        # def dp(n):
        #     # 查看备忘录，避免重复计算
        #     if n in memo: return memo[n]
        #     # base case
        #     if n == 0:
        #         return 0
        #     if n < 0:
        #         return -1
        #     res = float('INF')
        #     for coin in coins:
        #         subproblem = dp(n - coin)
        #         if subproblem == -1: continue
        #         res = min(res, 1 + subproblem)
        #     # 计入备忘录
        #     memo[n] = res if res != float('INF') else -1
        #     return memo[n]
        #
        # return dp(amount)

        """
        3.DP数组的迭代解法
        dp数组定义：当目标金额为i时，至少需要dp[i]枚凑出
        自底向上
        """
        # 初始化dp table
        dp = [float('INF')] * (amount + 1)
        # base case
        dp[0] = 0
        # 外层循环遍历所有状态的所有取值
        for i in range(1, amount + 1):
            # 内层循环求所有选择的最小值
            for coin in coins:
                if i - coin < 0: continue
                dp[i] = min(dp[i], 1 + dp[i-coin])
        if dp[-1] != float('INF'):
            return dp[-1]
        else:
            return -1

# leetcode submit region end(Prohibit modification and deletion)
