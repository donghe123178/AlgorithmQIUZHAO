# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。 
# 
#  示例: 
# 
#  输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ] 
# 
#  说明： 
# 
#  
#  所有输入均为小写字母。 
#  不考虑答案输出的顺序。 
#  
#  Related Topics 哈希表 字符串 
#  👍 396 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        """
        思路一：排序字符串相等时，两个字符串时字母异位词
        维护一个字典，将字符串排序，作为键，键是唯一的，值是一个列表，存储异位词
        时间复杂度：O(nklogk)
        空间复杂度：O(nk)
        """
        dic = {}
        for s in strs:
            key = ''.join(sorted(s))
            dic[key] = dic.get(key, []) + [s]
        return dic.values()
        """
        思路二：记数法，每个字符出现的次数相同时，两个字符串是字母异位词
        时间复杂度：O(nk)
        空间复杂度：O(nk)
        """
        # dic = {}
        # for s in strs:
        #     count = [0] * 26
        #     for c in s:
        #         count[ord(c) - ord('a')] += 1
        #     key = tuple(count)
        #     dic[key] = dic.get(key, []) + [s]
        # return dic.values()



# leetcode submit region end(Prohibit modification and deletion)
