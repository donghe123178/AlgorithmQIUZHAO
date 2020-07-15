# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。 
# 
#  你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。 
# 
#  
# 
#  示例: 
# 
#  给定 nums = [2, 7, 11, 15], target = 9
# 
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
#  
#  Related Topics 数组 哈希表 
#  👍 8635 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        1.暴力法,时间复杂度 O(n^2),空间复杂度O(1)
        拿数组里的第一个数字和后面的数字分别相加，看是否等于target；
        如果不等于target，那么就继续拿数组里的第二个数字和后面的数字相加；
        不停的去一个个试...直到等于target，返回这2个数字所在的下标
        """
        # for i in range(len(nums) - 1):
        #     b = target - nums[i]
        #     for j in range(i + 1, len(nums)):
        #         if b == nums[j]:
        #             return [i, j]
        # return []

        """
        2.一遍哈希表，时间复杂度 O(n),空间复杂度O(n)
        哈希表保证了查询是O(1)的
        """
        dic = {}
        for i, a in enumerate(nums):
            b = target - a
            if b in dic:
                return [i, dic[b]]
            dic[a] = i

# leetcode submit region end(Prohibit modification and deletion)
