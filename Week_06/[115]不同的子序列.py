# 给定一个字符串 S 和一个字符串 T，计算在 S 的子序列中 T 出现的个数。 
# 
#  一个字符串的一个子序列是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列
# ，而 "AEC" 不是） 
# 
#  题目数据保证答案符合 32 位带符号整数范围。 
# 
#  
# 
#  示例 1： 
# 
#  输入：S = "rabbbit", T = "rabbit"
# 输出：3
# 解释：
# 
# 如下图所示, 有 3 种可以从 S 中得到 "rabbit" 的方案。
# (上箭头符号 ^ 表示选取的字母)
# 
# rabbbit
# ^^^^ ^^
# rabbbit
# ^^ ^^^^
# rabbbit
# ^^^ ^^^
#  
# 
#  示例 2： 
# 
#  输入：S = "babgbag", T = "bag"
# 输出：5
# 解释：
# 
# 如下图所示, 有 5 种可以从 S 中得到 "bag" 的方案。 
# (上箭头符号 ^ 表示选取的字母)
# 
# babgbag
# ^^ ^
# babgbag
# ^^    ^
# babgbag
# ^    ^^
# babgbag
#   ^  ^^
# babgbag
#     ^^^ 
#  Related Topics 字符串 动态规划 
#  👍 241 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        """
        s是主串，t是子串
        动态规划：
        dp[i][j] = T[0：i]在s[0：j]中的子串个数
        dp[i][j] = dp[i-1][j-1] + dp[i][j-1],最后一个字符相同时
        dp[i][j] = dp[i][j-1]
        """
        m = len(t)
        n = len(s)
        dp = [[0] * (n+1) for _ in range(m+1)] # 因为考虑到空集，所以空间+1
        for i in range(m+1):
            for j in range(n+1):
                if i == 0:
                    dp[0][j] = 1
                if j == 0:
                    continue
                if t[i-1] == s[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[-1][-1]

        
# leetcode submit region end(Prohibit modification and deletion)
