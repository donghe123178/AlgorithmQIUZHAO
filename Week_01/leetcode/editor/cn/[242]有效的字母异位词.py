# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。 
# 
#  示例 1: 
# 
#  输入: s = "anagram", t = "nagaram"
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入: s = "rat", t = "car"
# 输出: false 
# 
#  说明: 
# 你可以假设字符串只包含小写字母。 
# 
#  进阶: 
# 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？ 
#  Related Topics 排序 哈希表 
#  👍 216 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isAnagram(self, s, t):
        """
        暴力法，排序后判断是否相等
        时间复杂度：O(nlogn)
        """
        # 异位词：字母出现的次数都是一样的
        # return sorted(s) == sorted(t)

        """
        用哈希表统计第一个字符串中的字符数量；
        再统计第二个字符串时，若字符在哈希表中，计数减一;
        当出现小于0时，返回False
        哈希精简写法
        时间复杂度：O(n)
        """
        if len(s) != len(t):
            return False
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1
        for c in t:
            d[c] = d.get(c, 0) - 1
            if d[c] < 0:
                return False
        return True


# leetcode submit region end(Prohibit modification and deletion)
