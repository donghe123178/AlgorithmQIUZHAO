# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。 
# 
#  
# 
#  示例： 
# 
#  输入：n = 3
# 输出：[
#        "((()))",
#        "(()())",
#        "(())()",
#        "()(())",
#        "()()()"
#      ]
#  
#  Related Topics 字符串 回溯算法 
#  👍 1226 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        """
        分析：
        想象成有2*n个格子，每个格子既可以插入左括号，又可以插入右括号，二叉树结构，n层
        1.插入括号的数量<=n
        2.可以插入右括号的前提是 剩下的左括号数量 < 右括号，说明放入的左括号>右括号
        DFS
        """
    #     res = []
    #     self.dfs(res, n, n, '')
    #     return res
    #
    # def dfs(self, res, left, right, path):
    #     if left == 0 and right == 0:
    #         res.append(path)
    #         return
    #     if left < 0:
    #         return
    #     if left > right:
    #         return
    #     self.dfs(res, left - 1, right, path + '(')
    #     self.dfs(res, left, right - 1, path + ')')

    # def dfs(self, res, left, right, path):
    #     if left == 0 and right == 0:
    #         res.append(path)
    #         return
    #     if left > 0:
    #         self.dfs(res, left - 1, right, path + '(')
    #     if left < right:
    #         self.dfs(res, left, right - 1, path + ')')
        """
        2.动态规划https://leetcode-cn.com/problems/generate-parentheses/solution/zui-jian-dan-yi-dong-de-dong-tai-gui-hua-bu-lun-da/
        数组dp[i],表示n=i时生成的有效括号组合
        递推公式：dp[i] = '(' + dp[m] + ')' + dp[k], m + k = i-1
        """
        dp = [0] * (n+1)
        dp0 = ''
        dp[0] = dp0
        for i in range(1, n+1):
            cur = []
            for i in range(i-1):
                k = i - 1

# leetcode submit region end(Prohibit modification and deletion)
