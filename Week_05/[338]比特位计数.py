# 给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。 
# 
#  示例 1: 
# 
#  输入: 2
# 输出: [0,1,1] 
# 
#  示例 2: 
# 
#  输入: 5
# 输出: [0,1,1,2,1,2] 
# 
#  进阶: 
# 
#  
#  给出时间复杂度为O(n*sizeof(integer))的解答非常容易。但你可以在线性时间O(n)内用一趟扫描做到吗？ 
#  要求算法的空间复杂度为O(n)。 
#  你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的 __builtin_popcount）来执行此操作。 
#  
#  Related Topics 位运算 动态规划 
#  👍 382 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        """
        复杂度分析：
        时间复杂度位O(N)
        空间复杂度位O(N)
        """
        # res = []
        # for i in range(num+1):
        #     res.append(bin(i).count('1'))
        # return res

        """
        动态规划：看最低有效位
        dp(x)，整数x，位1的个数
        dp(x) = dp(x>>=1) + (x & 1)， 右移一位+最低位，注意运算符的优先级
        复杂度分析：
        时间复杂度位O(N)
        空间复杂度位O(N)
        """
        dp = [0] * (num + 1)
        for i in range(1, num+1):
            dp[i] = dp[i>>1] + (i & 1)
        return dp

# leetcode submit region end(Prohibit modification and deletion)
