# 给定一个非负整数数组，你最初位于数组的第一个位置。 
# 
#  数组中的每个元素代表你在该位置可以跳跃的最大长度。 
# 
#  判断你是否能够到达最后一个位置。 
# 
#  示例 1: 
# 
#  输入: [2,3,1,1,4]
# 输出: true
# 解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
#  
# 
#  示例 2: 
# 
#  输入: [3,2,1,0,4]
# 输出: false
# 解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
#  
#  Related Topics 贪心算法 数组 
#  👍 764 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """
        贪心算法：
        从后往前遍历，如果当前值+当前索引(跳最远) >= 右边能达到的索引，则说明此子问题用最优解解决了
        下一个子问题继续用此方法，判断右边能达到的索引是否等于0
        时间复杂度为O(N)
        空间复杂度为O(1)
        """
        if not nums:
            return False
        position = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] + i >= position:
                position = i
        return position == 0

# leetcode submit region end(Prohibit modification and deletion)
