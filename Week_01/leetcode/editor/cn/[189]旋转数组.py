# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。 
# 
#  示例 1: 
# 
#  输入: [1,2,3,4,5,6,7] 和 k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]
#  
# 
#  示例 2: 
# 
#  输入: [-1,-100,3,99] 和 k = 2
# 输出: [3,99,-1,-100]
# 解释: 
# 向右旋转 1 步: [99,-1,-100,3]
# 向右旋转 2 步: [3,99,-1,-100] 
# 
#  说明: 
# 
#  
#  尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。 
#  要求使用空间复杂度为 O(1) 的 原地 算法。 
#  
#  Related Topics 数组 
#  👍 622 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        """
        1.暴力法，旋转K次，每次旋转1次
        时间复杂度O(K*n)的, 空间复杂度0(1) 会超出时间限制
        """
        # k = k % len(nums)
        # for i in range(0, k):
        #     previous = nums[len(nums) - 1]
        #     for j in range(0, len(nums)):
        #         temp = nums[j]
        #         nums[j] = previous
        #         previous = temp
        """
        2.切片操作，空间复杂度为O(N)，时间复杂度？
        """
        # n = len(nums)
        # k = k % n   # 求余
        # return nums[-k:] + nums[:-k]
        """
        3.环状替换
        时间复杂度O(N),空间复杂度O(1)
        """
        k %= len(nums)
        count = 0

        for i in range(len(nums)):
            current = i
            previous = nums[i]
            while i != current:
                next = (current + k) % len(nums)
                temp = nums[next]
                nums[next] = previous
                previous = temp
                current = next
                count += 1
# 没懂环状替换
# leetcode submit region end(Prohibit modification and deletion)
