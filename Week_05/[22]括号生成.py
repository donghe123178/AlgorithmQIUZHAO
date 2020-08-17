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
        if not n:
            return []
        res = []

        def backtrace(n, tmp):
            if len(tmp) == 2 * n:
                res.append(tmp[:])
                return
            if tmp.count('(') < n:
                tmp.append('(')
                backtrace(n, tmp)
                tmp.pop()
            if tmp.count(')') < tmp.count('('):
                tmp.append(')')
                backtrace(n, tmp)
                tmp.pop()

        backtrace(n, [])
        res = [''.join(i) for i in res]
        return res

# leetcode submit region end(Prohibit modification and deletion)
