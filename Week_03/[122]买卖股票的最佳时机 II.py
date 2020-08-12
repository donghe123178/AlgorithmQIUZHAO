# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。 
# 
#  设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。 
# 
#  注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。 
# 
#  
# 
#  示例 1: 
# 
#  输入: [7,1,5,3,6,4]
# 输出: 7
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
#      随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
#  
# 
#  示例 2: 
# 
#  输入: [1,2,3,4,5]
# 输出: 4
# 解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
#      注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
#      因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
#  
# 
#  示例 3: 
# 
#  输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= prices.length <= 3 * 10 ^ 4 
#  0 <= prices[i] <= 10 ^ 4 
#  
#  Related Topics 贪心算法 数组 
#  👍 805 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """
        分析题目：不限制交易次数了，买股票，卖股票，这一接连行为可以发生k次
        关键在于何时买，何时卖，使得利润最大
        暴力搜索
        想象自己每天醒来检查自己有股票吗，然后看股市
        1.没股票时，买股票，或者无操作
        2.有股票，卖股票，或者无操作
        3.记录自己的花费
        4.最后一天，清算自己赚了多少钱
        穷举所有的可能性
        """

        """
        贪心算法：
        理解：相当于开天眼了，如果今天买，明天卖的利润大于0，就执行买卖操作，否则不进行操作
        把利润累加起来，就是最大利润       
        复杂度分析：
        时间复杂度为O(N)
        空间复杂度为O(1)
        """
        # profit = 0
        # for i in range(len(prices)):
        #     if i == 0:
        #         continue
        #     tmp = prices[i] - prices[i-1]
        #     if tmp > 0:
        #         profit += tmp
        # return profit

        """
        动态规划：
        子问题有两种状态，持有股票，没有股票，
        数组dp：第一天到当天的最大利润，最后一天的状态肯定是没有股票
        递推方程：
        """
        n = len(prices)
        dp_i_0 = 0
        dp_i_1 = int(-1e9)
        for i in range(n):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, dp_i_0 - prices[i])
        return dp_i_0



# leetcode submit region end(Prohibit modification and deletion)
