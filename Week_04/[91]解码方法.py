# 一条包含字母 A-Z 的消息通过以下方式进行了编码： 
# 
#  'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
#  
# 
#  给定一个只包含数字的非空字符串，请计算解码方法的总数。 
# 
#  示例 1: 
# 
#  输入: "12"
# 输出: 2
# 解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
#  
# 
#  示例 2: 
# 
#  输入: "226"
# 输出: 3
# 解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
#  
#  Related Topics 字符串 动态规划 
#  👍 462 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        动态规划：
        dp数组：dp[i]: s[0:i]的解码总数,取不到s[i],只能取到s[i-1]
        递推方程：
        1.s[i]=0
            合并解码：s[i-1] = 1 or 2: dp[i+1]=dp[i-1]
            其他无法解码：return 0
        2.s[i]!=0
            合并+单独解码：  10 < s[i-1][i] < 27: dp[i+1] = dp[i]+dp[i-1]
            其他单独解码：dp[i+1] = dp[i] 
        复杂度分析：
        时间空间复杂度均为O(N)  
        """
        if not s or s[0] == '0':
            return 0
        n = len(s)
        dp = [1] * (n + 1)
        for i in range(n):
            if i == 0:
                continue
            if s[i] == '0':
                if s[i - 1] == '1' or s[i - 1] == '2':
                    dp[i + 1] = dp[i-1]
                else:
                    return 0
            else:
                if 10 < int(s[i - 1:i + 1]) < 27:
                    dp[i + 1] = dp[i] + dp[i - 1]
                else:
                    dp[i + 1] = dp[i]
        return dp[-1]

        """
        空间优化，dp[i + 1]，dp[i]，dp[i-1]，用变量代替
        空间复杂度降为O(1)
        """
        # if not s or s[0] == '0':
        #     return 0
        # n = len(s)
        # cur = 1  # 计算前是dp[i], 计算后是dp[i + 1]
        # pre = 1  # dp[i-1]
        # for i in range(n):
        #     tmp = cur
        #     if i == 0:
        #         continue
        #     if s[i] == '0':
        #         if s[i - 1] == '1' or s[i - 1] == '2':
        #             cur = pre
        #         else:
        #             return 0
        #     else:
        #         if 10 < int(s[i - 1:i + 1]) < 27:
        #             cur += pre
        #     pre = tmp
        # return cur


if __name__ == '__main__':
    a = Solution()
    b = a.numDecodings("0")
    # s = "226"
    # c = int(s[1] + s[2])
    print(b)
    # for i in range(1):
    #     print(i)

# leetcode submit region end(Prohibit modification and deletion)
