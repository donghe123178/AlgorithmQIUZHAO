# 给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。 
# 
#  说明：不要使用任何内置的库函数，如 sqrt。 
# 
#  示例 1： 
# 
#  输入：16
# 输出：True 
# 
#  示例 2： 
# 
#  输入：14
# 输出：False
#  
#  Related Topics 数学 二分查找 
#  👍 156 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        """
        分析：完全平方数，就是存在整数x,使得x^2 = num，用二分查找法
        """
        left, right = 1, num
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == num:
                return True
            if mid * mid > num:
                right = mid - 1
            else:
                left = mid + 1
        return False

# leetcode submit region end(Prohibit modification and deletion)
