# 实现 pow(x, n) ，即计算 x 的 n 次幂函数。 
# 
#  示例 1: 
# 
#  输入: 2.00000, 10
# 输出: 1024.00000
#  
# 
#  示例 2: 
# 
#  输入: 2.10000, 3
# 输出: 9.26100
#  
# 
#  示例 3: 
# 
#  输入: 2.00000, -2
# 输出: 0.25000
# 解释: 2-2 = 1/22 = 1/4 = 0.25 
# 
#  说明: 
# 
#  
#  -100.0 < x < 100.0 
#  n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。 
#  
#  Related Topics 数学 二分查找 
#  👍 457 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        """
        1.暴力法
        时间复杂度o(n)
        空间复杂度o(1)
        """

        """"
        2.分治法,递归
        时间复杂度O(logn)
        空间复杂度O(logn)
        考虑边界条件:
        如果 n 是负数，那么相当于求 (1/x)^(-n)。
        如果 n 是正数 且 奇数，那么结果需要单独乘以 x
        如果 n 是正数 且 偶数，求(x^2)^(n/2)，一直递归下去即可
        """
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        if n % 2:
            return x * self.myPow(x, n - 1)
        return self.myPow(x * x, n / 2)
        """
        3.迭代
        时间复杂度是O(logn)，空间复杂度是O(1)
        """
        # if n == 0:
        #     return 1
        # if n < 0:
        #     x = 1 / x
        #     n = -n
        # ans = 1
        # while n:
        #     if n % 2 != 0:
        #         ans *= x
        #     n >>= 1
        #     x *= x
        # return ans



# leetcode submit region end(Prohibit modification and deletion)
