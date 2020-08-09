# 给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。 
# 
#  具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。 
# 
#  示例 1: 
# 
#  
# 输入: "abc"
# 输出: 3
# 解释: 三个回文子串: "a", "b", "c".
#  
# 
#  示例 2: 
# 
#  
# 输入: "aaa"
# 输出: 6
# 说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".
#  
# 
#  注意: 
# 
#  
#  输入的字符串长度不会超过1000。 
#  
#  Related Topics 字符串 动态规划 
#  👍 294 👎 0

# 优秀题解：https://leetcode-cn.com/problems/palindromic-substrings/solution/liang-dao-hui-wen-zi-chuan-de-jie-fa-xiang-jie-zho/
# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        分析：
        首先要判断是否是回文子串
        动态规划：
        dp数组：dp[i][j]，表示s[i：j+1]区间的字串是否是一个回文串
        递推方程：
        当s[i] = s[j] and (j-i < 2 or dp[i+1][j-1])时，dp[i][j]=true
        1.只有一个字符
        2.两个字符
        3.三个字符及其以上
        复杂度分析：时间空间复杂度均为O(N^2)
        # """
        # dp = [[0]*len(s) for _ in range(len(s))]
        # res = 0
        # for j in range(len(s)):
        #     for i in range(j+1):
        #         if s[i] == s[j] and (j-i < 2 or dp[i+1][j-1]):
        #             dp[i][j] = True
        #             res += 1
        # return res

        """
        中心扩展法：left指针，中心点，right指针，s[left] = s[ritht]
        中心点：
            单字符，aba，个数len（s），初始化时，left = right
            双字符, baab，个数len（s）-1，初始化时，left +1 = ritht
            总共2len-1个
        时间复杂度位O(N^2),空间复杂度位为O(1)
        """
        res = 0
        for center in range(2 * (len(s)) - 1):
            left = center / 2
            right = left + center % 2  # center为奇数时，中心点取双字符，为偶数时，取单字符
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
        return res
# leetcode submit region end(Prohibit modification and deletion)
