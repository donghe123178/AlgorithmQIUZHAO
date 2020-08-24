# 数组的每个索引作为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。 
# 
#  每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。 
# 
#  您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。 
# 
#  示例 1: 
# 
#  输入: cost = [10, 15, 20]
# 输出: 15
# 解释: 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。
#  
# 
#  示例 2: 
# 
#  输入: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# 输出: 6
# 解释: 最低花费方式是从cost[0]开始，逐个经过那些1，跳过cost[3]，一共花费6。
#  
# 
#  注意： 
# 
#  
#  cost 的长度将会在 [2, 1000]。 
#  每一个 cost[i] 将会是一个Integer类型，范围为 [0, 999]。 
#  
#  Related Topics 数组 动态规划 
#  👍 357 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        """
        时间复杂度O(N)
        空间复杂度O(N)
        """
        # n = len(cost)
        # dp = [0] * n  # 从0爬上第n台阶所对应的最小体力花费
        # for i in range(n):
        #     if i == 0:
        #         continue
        #     if i == 1:
        #        dp[1] = min(cost[0], cost[1])
        #     else:
        #         dp[i] = min(dp[i-1] + cost[i], dp[i-2] + cost[i-1]) # 爬1步， 爬两步
        # return dp[-1]

        # 空间优化
        dp1, dp2, res = 0, 0, 0
        for i in range(len(cost)):
            if i == 0:
                continue
            if i == 1:
                res = min(cost[0], cost[1])
                dp1 = res
            else:
                res = min(dp1 + cost[i], dp2 + cost[i-1])
                dp1, dp2 = res, dp1
        return res

        
# leetcode submit region end(Prohibit modification and deletion)
