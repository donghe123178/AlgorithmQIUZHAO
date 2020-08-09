# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。 
# 
#  示例 1: 
# 
#  输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"
#  
# 
#  示例 2: 
# 
#  输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"
#  
#  Related Topics 字符串 动态规划 
#  👍 891 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        动态规划：
        dp数组：dp[i]，表示s[:i+1]字符子串，以i结尾的最长有效括号的长度
        递推方程：
        1.s[i] = '(', dp[i] = 0
        2.s[i] = ')'
            s[i-1] = '('，dp[i] = dp[i-2] + 2
            s[i-1] = ')'，并且s[i-dp[i-1]-1] = '(', dp[i] = dp[i-1] + 2 + dp[i-dp[i-1] -2]
        复杂度分析：
        时间复杂度O(N)
        """
        # res = 0
        # dp = [0] * (len(s) + 1)
        # for i in range(0, len(s)):
        #     if i > 0 and s[i] == ')':
        #         if s[i - 1] == '(':
        #             dp[i + 1] = dp[i - 1] + 2
        #         elif s[i - 1] == ')' and i - dp[i] - 1 >= 0 and s[i - dp[i] - 1] == '(':
        #             # 这里要特别注意dp[i - dp[i] - 1]，因为多了dp比s多了1
        #             dp[i + 1] = dp[i] + 2 + dp[i - dp[i] - 1]
        #         res = max(res, dp[i + 1])
        # return res

        # 疑问？为什么是dp[i-2]不会报错, i = 0时，dp[-1] = 0
        res = 0
        dp = [0] * len(s)
        for i in range(0, len(s)):
            if i > 0 and s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2
                elif s[i - 1] == ')' and i - dp[i-1] - 1 >= 0 and s[i - dp[i-1] - 1] == '(':
                    dp[i] = dp[i-1] + 2 + dp[i - dp[i-1] - 2]
                res = max(res, dp[i])
        return res

if __name__ == '__main__':
    a = Solution()
    c = a.longestValidParentheses("()")
    print(c)


# leetcode submit region end(Prohibit modification and deletion)
