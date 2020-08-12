# 给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：
#  
# 
#  
#  每次转换只能改变一个字母。 
#  转换过程中的中间单词必须是字典中的单词。 
#  
# 
#  说明: 
# 
#  
#  如果不存在这样的转换序列，返回 0。 
#  所有单词具有相同的长度。 
#  所有单词只由小写字母组成。 
#  字典中不存在重复的单词。 
#  你可以假设 beginWord 和 endWord 是非空的，且二者不相同。 
#  
# 
#  示例 1: 
# 
#  输入:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# 
# 输出: 5
# 
# 解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
#      返回它的长度 5。
#  
# 
#  示例 2: 
# 
#  输入:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# 
# 输出: 0
# 
# 解释: endWord "cog" 不在字典中，所以无法进行转换。 
#  Related Topics 广度优先搜索 
#  👍 400 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        """
        分析：BFS
        最想想到：从字典中提取出 单词中每个位置可能出现的字母 存在一个 集合里
        会超时
        """
        # if endWord not in wordList:
        #     return 0
        # m = len(beginWord)
        # for i in range(m):
        #     l.append([])
        # for word in wordList:
        #     for i in range(m):
        #         l[i].append(word[i])
        # new_list = map(set, l)
        # queue = [(beginWord, 1)]
        # while queue:
        #     currentWord, step = queue.pop(0)
        #     if currentWord == endWord:
        #         return step
        #     for i, letter in enumerate(currentWord):
        #         for j in new_list[i]:
        #             temp = currentWord[:i] + j + currentWord[i+1:]
        #             if temp in wordList:
        #                 queue.append((temp, step + 1))
        #                 wordList.remove(temp)
        # return 0

        """
        改进：
        用dict存储，从字典中找出单词的所有的通用状态，将单词中的某个字母用*代替，作为key, value就是具有通用特征的单词
        {'D*g':[Dog, Dig], 'H*t':[Hit, Hot]}
        复杂度分析：
        时间复杂度为O(M*N),M是单词的长度，N是单词标中单词的总数
        空间复杂度为O(M*N)
        """
        if endWord not in wordList or not beginWord or not endWord or not wordList:
            return 0
        n = len(beginWord)
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(n):
                all_combo_dict[word[:i] + '*' + word[i + 1:]].append(word)
        queue = [(beginWord, 1)]
        visited = {beginWord: True}
        while queue:
            current_word, step = queue.pop(0)
            for i in range(n):
                temp = current_word[:i] + '*' + current_word[i+1:]
                for word in all_combo_dict[temp]:
                    if word == endWord:
                        return step + 1
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, step + 1))
            all_combo_dict[temp] = []
        return 0


if __name__ == '__main__':

    l = defaultdict(list)
    l["1"].append("2")
    l["1"].append("3")
    print(l)

# leetcode submit region end(Prohibit modification and deletion)
