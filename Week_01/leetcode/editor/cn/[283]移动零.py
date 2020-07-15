# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。 
# 
#  示例: 
# 
#  输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0] 
# 
#  说明: 
# 
#  
#  必须在原数组上操作，不能拷贝额外的数组。 
#  尽量减少操作次数。 
#  
#  Related Topics 数组 双指针 
#  👍 649 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        """
        空间复杂度为O(1)
        1.两次遍历，
        第一次，找出所有的非零元素，就是移动一个指针，将非零元素从数组开头挨着放
        第二次遍历，给剩下的元素赋值为0
        时间复杂度0(n)
        """
        # j = 0 # 记录非零元素
        # for i in range(len(nums)):
        #     if nums[i]:
        #         nums[j] = nums[i]
        #         j += 1
        # for i in range(j, len(nums)):
        #     nums[i] = 0
        """
        2. 用双指针,遍历数组，慢指针记录零元素的位置，快指针找非零元素，然后交换，指针滑动
        时间复杂度O(N)
        """
        j = 0
        for i in range(len(nums)):
            if nums[i]: # 快指针的值不为0就交换，之后慢指针指向下一个指针值为0的位置
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
# leetcode submit region end(Prohibit modification and deletion)
