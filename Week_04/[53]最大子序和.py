# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。 
# 
#  示例: 
# 
#  输入: [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
#  
# 
#  进阶: 
# 
#  如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。 
#  Related Topics 数组 分治算法 动态规划 
#  👍 2267 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        1.c=a+b,如果c<b,则抛弃掉a，即指向a的指针前移动，否则指向b的指针向前移动
        2.状态空间记录最大值
        """
        # 1.暴力法，枚举起点和终点
        # if not nums:
        #     return
        # li = []
        # for start in range(len(nums)):
        #     res = 0
        #     for end in range(start, len(nums)):
        #         res += nums[end]
        #         res = max(res, nums[end])
        #         li.append(res)
        # return max(li)
        """
        DP:
        分治（子问题）max_sum(i) = max(max_sub(i-1), 0) + a[i]
        状态数组定义 f(i)
        DP方程：f[i] =max(f[i-1]+a[i], a[i])=max(f[i-1], 0) + a[i]
        小于零的数丢掉
        最大子序和 = 当前元素自身最大，或者包含之前后最大
        """
        # 自底向上
        dp = nums
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i-1])
        return max(dp)

        # 复用空间，工程上不推荐
        # for i in range(1, len(nums)):
        #     nums[i] = max(nums[i], nums[i-1] + nums[i])
        # return max(nums)


# leetcode submit region end(Prohibit modification and deletion)
