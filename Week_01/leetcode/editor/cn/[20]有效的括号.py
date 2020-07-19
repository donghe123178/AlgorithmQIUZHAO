# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。 
# 
#  有效字符串需满足： 
# 
#  
#  左括号必须用相同类型的右括号闭合。 
#  左括号必须以正确的顺序闭合。 
#  
# 
#  注意空字符串可被认为是有效字符串。 
# 
#  示例 1: 
# 
#  输入: "()"
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入: "()[]{}"
# 输出: true
#  
# 
#  示例 3: 
# 
#  输入: "(]"
# 输出: false
#  
# 
#  示例 4: 
# 
#  输入: "([)]"
# 输出: false
#  
# 
#  示例 5: 
# 
#  输入: "{[]}"
# 输出: true 
#  Related Topics 栈 字符串 
#  👍 1686 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        """
        最近相关性，洋葱性的题目，用栈的数据结构
        1.暴力法，不断用空字符去替换，直到整个字符串为空
        时间复杂度为O(N^2)
        """
        # for i in range(len(s)-1):
        #     for j in range(i, len(s)):
        #         if s[i] == [j]:
        #             s.replace(s[i],'')
        # if not s:
        #     return True
        """
        2.栈，时间空间复杂度都为O(n)
        """
        # if len(s) % 2 != 0:
        #     return False
        stack = []
        dic = {")": "(", "}": "{", "]": "["}
        for char in s:
            if stack and char in dic:
                if stack[-1] == dic [char]:
                    stack.pop()
            else:
                stack.append(char)
        return not stack


# leetcode submit region end(Prohibit modification and deletion)
