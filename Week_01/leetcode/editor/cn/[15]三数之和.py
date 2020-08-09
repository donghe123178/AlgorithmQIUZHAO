# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复
# 的三元组。 
# 
#  注意：答案中不可以包含重复的三元组。 
# 
#  
# 
#  示例： 
# 
#  给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# 
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
#  
#  Related Topics 数组 双指针 
#  👍 2372 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        """
        a + b = -c
        三元组不重复，判重？
        1.暴力法，三重循环O(N^3)
        2.由于题目没要求返回下标，因此可将列表排序，O(NlogN)
        3.双指针法，夹逼，时间复杂度O(N^2)，空间复杂度O(1)
        """
        nums.sort()
        res = []  # 存放结果
        k = 0  # 固定最小值
        for k in range(len(nums) - 2):
            if nums[k] > 0: break  # 排序之后，k代表的值是最小的 
            if k > 0 and nums[k] == nums[k - 1]: continue  # 跳过重复的nums[k]
            i, j = k + 1, len(nums) - 1
            while i < j:
                s = nums[k] + nums[i] + nums[j]
                if s < 0:
                    i += 1
                    while i < j and nums[i] == nums[i - 1]: i += 1  # 跳过重复的nums[i]
                elif s > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1  # 跳过重复的nums[j]
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1
        return res


# leetcode submit region end(Prohibit modification and deletion)
