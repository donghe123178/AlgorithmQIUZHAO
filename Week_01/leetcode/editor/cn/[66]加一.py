# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。 
# 
#  最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。 
# 
#  你可以假设除了整数 0 之外，这个整数不会以零开头。 
# 
#  示例 1: 
# 
#  输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。
#  
# 
#  示例 2: 
# 
#  输入: [4,3,2,1]
# 输出: [4,3,2,2]
# 解释: 输入数组表示数字 4321。
#  
#  Related Topics 数组 
#  👍 502 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        """
        分析：数字9加一，进位
        1. 一遍循环，时间复杂度
        """
        # for i in range(len(digits)-1, -1, -1):
        #     if digits[i] != 9:
        #         digits[i] += 1
        #         return digits
        #     else:
        #         digits[i] = 0
        #         if digits[0] is 0:
        #             digits.insert(0, 1)
        #             return digits
        """
        2.转换为数字，计算，再转换为数组
        """
        a = [i * 10 ** index for index, i in enumerate(digits[::-1])]
        num = sum(a) + 1
        return [int(x) for x in str(num)]


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print([i for i in range(3, -1, -1)])
