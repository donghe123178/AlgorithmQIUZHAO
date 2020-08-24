# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。 
# 
#  示例 1： 
# 
#  输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
#  
# 
#  示例 2： 
# 
#  输入: "cbbd"
# 输出: "bb"
#  
#  Related Topics 字符串 动态规划 
#  👍 2534 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        1.暴力法：枚举子串起点和中点
        时间复杂度O(N^3)
        """
        """
        2.枚举中心，中心扩展法
        注意可以是偶数长度，也可以是奇数长度，中心点位置的确定及个数
        时间复杂度为O(n^2)
        """
        res = ""
        for center in range(2 * len(s) - 1):
            left = center / 2
            right = left + center % 2
            while left >= 0 and right < len(s) and s[left] == s[right]:
                tmp = s[left:right + 1]
                if len(tmp) > len(res):
                    res = tmp
                left -= 1
                right += 1
        return res

        """
        3.动态规划
        dp[i][j],表示s[i:j]是否为回文串，取闭区间，i<=j
        dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]
        边界条件i-j<=2
        初始化，i=j时，true，对角线为true
        输出，为true时，记录子串的长度和起始位置
        复杂度分析：
        时间复杂度为O(N^2)
        空间复杂度为O(N^2)
        """
        n = len(s)
        if n < 2:
            return s
        dp = [[False] * (n + 1) for _ in range(n + 1)]
        max_len = 1
        start = 0
        for j in range(1, n):
            for i in range(0, j):
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True  # 不构成区间
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False
                if dp[i][j]:
                    cur_len = j - i + 1
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i

        return s[start:start + max_len]
# leetcode submit region end(Prohibit modification and deletion)
