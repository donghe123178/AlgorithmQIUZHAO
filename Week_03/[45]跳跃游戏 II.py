# 给定一个非负整数数组，你最初位于数组的第一个位置。 
# 
#  数组中的每个元素代表你在该位置可以跳跃的最大长度。 
# 
#  你的目标是使用最少的跳跃次数到达数组的最后一个位置。 
# 
#  示例: 
# 
#  输入: [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
#      从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
#  
# 
#  说明: 
# 
#  假设你总是可以到达数组的最后一个位置。 
#  Related Topics 贪心算法 数组 
#  👍 654 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        贪心算法：通过局部最优得到全局最优解
        贪心策略：反向查找，选择距离最后一个位置最远的那个位置，下标最小，直到数组的开始位置
        返回steps
        时间复杂度为O(N^2),会超时
        空间复杂度为O(1)
        """
        # position = len(nums) - 1
        # steps = 0
        # while position > 0:
        #     for i in range(position):
        #         if i + nums[i] >= position:
        #             position = i
        #             steps += 1
        #             break
        # return steps

        """
        贪心策略：正向查找
        时间复杂为O(N)
        空间复杂度为O(1)
        """
        max_pos, end, steps = 0, 0, 0
        for i in range(len(nums)-1):
            if max_pos >= i:
                max_pos = max(max_pos, i + nums[i])  # 维护能够达到的最大下标位置，直到被超越
                if i == end:  # 这里太巧妙了，需要多理解，对于[2, 3, 1, 2, 4, 2, 3],0,2,4,跳三次
                    end = max_pos
                    steps += 1
        return steps


# leetcode submit region end(Prohibit modification and deletion)
