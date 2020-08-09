# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。 
# 
#  如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。 
# 
#  注意：你不能在买入股票前卖出股票。 
# 
#  
# 
#  示例 1: 
# 
#  输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
#  
# 
#  示例 2: 
# 
#  输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
#  
#  Related Topics 数组 动态规划 
#  👍 1121 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """
        题目理解：数组表示股票，数组的值表示股票价格，索引+1表示日期
        求的是re = prices[j] - prices[i],其中j>i,re>0,且re在所有的组合中是最大的
        1.暴力法
        时间复杂度为O(N^2),空间复杂度为O(1)
        """
        # res = 0
        # for i in range(len(prices)-1):
        #     for j in range(i + 1, len(prices)):
        #         res = max(res, prices[j] - prices[i])
        # return res
        """
        2.一次遍历，记录从第0天到第i天的最低价，记录下遍历过程中的利润最大值
        时间复杂度为O(N)
        空间复杂度为O(1)
        """
        # min_price = int(1e9)
        # max_profit = 0
        # for price in prices:
        #     min_price = min(price, min_price)
        #     # 包含了当天买当天卖（当天是最小的）的情况
        #     max_profit = max(max_profit, price - min_price)
        # return max_profit

        """
        3.动态规划
        dp数组的含义：第i天（包括i天）之前的利润
        空间复杂度为O(N)
        """
        # 为空的情况
        # if not prices:
        #     return 0
        # n = len(prices)
        # dp = [[0] * 2 for _ in range(n)]
        # for i in range(n):
        #     if i == 0:
        #         dp[i][0] = 0
        #         dp[i][1] = - prices[i]
        #     else:
        #         dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        #         dp[i][1] = max(dp[i - 1][1], - prices[i])
        # return dp[n - 1][0]


        # if not prices:
        #     return 0
        n = len(prices)
        dp_i_0 = 0
        dp_i_1 = int(-1e9)
        for i in range(n):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, - prices[i])
        return dp_i_0



# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    a = Solution()
    b = [7,1,5,3,6,4]
    c = a.maxProfit(b)
    print(c)