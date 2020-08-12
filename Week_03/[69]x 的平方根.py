# 实现 int sqrt(int x) 函数。 
# 
#  计算并返回 x 的平方根，其中 x 是非负整数。 
# 
#  由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。 
# 
#  示例 1: 
# 
#  输入: 4
# 输出: 2
#  
# 
#  示例 2: 
# 
#  输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842..., 
#      由于返回类型是整数，小数部分将被舍去。
#  
#  Related Topics 数学 二分查找 
#  👍 467 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        """
        1.二分查找：x = y^2，求y，y>0,y是整数。x抛物线，单调递增的，有上下界，非负整数，则范围：1~x
        因此，可以用二分查找求出y
        时间复杂度为O(logn)
        """
        if x == 0 or x == 1:
            return x
        left, right = 1, x
        while left <= right:
            mid = (left + right) / 2
            if mid * mid == x:
                return mid
            if mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1
        # 思考为什么要返回right,而不是left,因为循环跳出的原因，
        # 第一步，left = right, 第二步，是right - 1 < left,返回较小的那位
        return right

        """
        牛顿迭代法，思想：切线是曲线的逼近，不断迭代，使得切线的根逼近曲线的根（和x轴的交点）
        迭代方程：
        x_1 = x_o - y(x_0)/k(x_o)，k = 2x_0是斜率，x是根，y=x_0 * x_0 - a
        """
        # 1. 假定初始根
        r = x
        while r * r > x:
            r = (r + x/r) / 2
        return r

# leetcode submit region end(Prohibit modification and deletion)
