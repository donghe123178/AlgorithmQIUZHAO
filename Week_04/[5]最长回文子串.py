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
        中心扩展法
        """
        res = ""
        for center in range(2*len(s) -1):
            left = center / 2
            right = left + center % 2
            while left >=0 and right < len(s) and s[left] == s[right]:
                tmp = s[left:right+1]
                if len(tmp) > len(res):
                    res = tmp
                left -= 1
                right += 1
        return res
# leetcode submit region end(Prohibit modification and deletion)
