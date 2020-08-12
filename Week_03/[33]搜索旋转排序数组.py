# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。 
# 
#  ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。 
# 
#  搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。 
# 
#  你可以假设数组中不存在重复的元素。 
# 
#  你的算法时间复杂度必须是 O(log n) 级别。 
# 
#  示例 1: 
# 
#  输入: nums = [4,5,6,7,0,1,2], target = 0
# 输出: 4
#  
# 
#  示例 2: 
# 
#  输入: nums = [4,5,6,7,0,1,2], target = 3
# 输出: -1 
#  Related Topics 数组 二分查找 
#  👍 871 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        """
        二分搜索，旋转之后的数组，被拆成了两部分，每一部分都是有序的
        1.nums[mid] < nums[mid + 1]，nums[mid] < nums[mid-1]，nums[mid]是最小值
        2.nums[mid] == target,返回nums.index(target)
        3.nums[0] <= nums[mid],[0:mid+1]，一定单调递增，
        4.当nums[0] > nums[mid], [mid+1: -1],一定单调递增
        5.每一个部分用二分查找法
        复杂度分析：
        时间复杂度：O(logN)
        空间复杂度为O(1)
        """
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # 首先判断nums[mid]落在哪个区域，再确定target在哪个区域
            # 注意这里的等号
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[-1]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

# leetcode submit region end(Prohibit modification and deletion)
