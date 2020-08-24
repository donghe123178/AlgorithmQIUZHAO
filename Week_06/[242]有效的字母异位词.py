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
#  👍 237 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 1.调用系统函数，排序 nlogn
        # s = sorted(s)
        # t = sorted(t)
        # if s == t:
        #     return True
        # else:
        #     return False

        # 2.哈希表，统计字母出现的个数，3n
        # dic = {}
        # for i in s:
        #     dic[i] = dic.get(i, 0) + 1
        # for i in t:
        #     dic[i] = dic.get(i, 0) - 1
        # for value in dic.values():
        #     if value != 0:
        #         return False
        # return True

        # 3.首先判断长度
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

        dic = {}
# leetcode submit region end(Prohibit modification and deletion)
