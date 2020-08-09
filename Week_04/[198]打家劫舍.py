# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上
# 被小偷闯入，系统会自动报警。 
# 
#  给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[1,2,3,1]
# 输出：4
# 解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
#      偷窃到的最高金额 = 1 + 3 = 4 。 
# 
#  示例 2： 
# 
#  输入：[2,7,9,3,1]
# 输出：12
# 解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
#      偷窃到的最高金额 = 2 + 9 + 1 = 12 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 100 
#  0 <= nums[i] <= 400 
#  
#  Related Topics 动态规划 
#  👍 995 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        动态规划：
        自底向上的dp数组
        1.子问题：
        偷n个所有房子的最大金额转化为偷第1~k个房间的最大金额，f(k)，用dp数组存储
        2.递推关系：
        分析题目，偷房子两种情况：第K个房子偷还是不偷
        f(k) = max(f(k-2)+nums[k-1], f(k-1))
        3.数组表示
        dp[k] = max(dp[k-2] + nums[k-1], dp[k-1])
        边界条件：
        房子不存在，返回0
        第0个房子，dp[0] = 0
        第1个房子，dp[1] = nums[0]
        4.复杂度分析：
        时间空间复杂度均为O(n)
        """
        # n = len(nums)
        # if n == 0:
        #     return 0
        # dp = [0] * (n + 1)
        # dp[0] = 0
        # dp[1] = nums[0]
        # for k in range(2, n+1):
        #     dp[k] = max(dp[k-1], dp[k-2] + nums[k-1])
        # return dp[n]

        """
        空间优化，两个变量保存子结果
        空间复杂度O(1)
        """
        pre = 0
        cur = 0
        for i in nums:
            # pre, cur = cur, max(cur, pre + i)
            # 计算的是K个房间的最大金额，此时，cur代表f(k-1), pre代表f（k-2）
            tmp = max(cur, pre + i)
            pre = cur  # 保存偷 k-1 个房间的最大金额
            cur = tmp  # 保存偷 k 个房间的最大金额

        return cur





# leetcode submit region end(Prohibit modification and deletion)
