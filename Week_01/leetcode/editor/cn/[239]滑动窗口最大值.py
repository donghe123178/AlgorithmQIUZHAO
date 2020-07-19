# 给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。 
# 
# 
#  返回滑动窗口中的最大值。 
# 
#  
# 
#  进阶： 
# 
#  你能在线性时间复杂度内解决此题吗？ 
# 
#  
# 
#  示例: 
# 
#  输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
# 输出: [3,3,5,5,6,7] 
# 解释: 
# 
#   滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10^5 
#  -10^4 <= nums[i] <= 10^4 
#  1 <= k <= nums.length 
#  
#  Related Topics 堆 Sliding Window 
#  👍 455 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        """
        1.暴力法，遍历每个滑动窗口，找到每个窗口的最大值
        时间复杂度:O(n*k)
        空间复杂度：O(n-k+1)
        """
        # n = len(nums)
        # if n * k == 0:
        #     return []
        # # 列表生成式
        # return [max(nums[i: i + k]) for i in range(n - k + 1)]

        """
        2.双端队列，存的是数组的索引，关键在于何时进，何时出
        时间复杂度：O(N)
        空间复杂度：O(N)
        """
        # 边界值处理
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums

        res = []
        window = deque()
        for i in range(n):
            # 当有元素索引要进队列时，从队右边移除队列中比当前元素小的数
            while window and nums[i] > nums[window[-1]]:
                window.pop()
            # 当元素从左边界滑出的时候，如果恰恰是滑动窗口的最大值，则将其弹出
            if window and i - k == window[0]:
                window.popleft()
            # 从队右边进队
            window.append(i)
            if i >= k-1:
                res.append(nums[window[0]])
        return res

# leetcode submit region end(Prohibit modification and deletion)
