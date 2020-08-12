# 一条基因序列由一个带有8个字符的字符串表示，其中每个字符都属于 "A", "C", "G", "T"中的任意一个。 
# 
#  假设我们要调查一个基因序列的变化。一次基因变化意味着这个基因序列中的一个字符发生了变化。 
# 
#  例如，基因序列由"AACCGGTT" 变化至 "AACCGGTA" 即发生了一次基因变化。 
# 
#  与此同时，每一次基因变化的结果，都需要是一个合法的基因串，即该结果属于一个基因库。 
# 
#  现在给定3个参数 — start, end, bank，分别代表起始基因序列，目标基因序列及基因库，请找出能够使起始基因序列变化为目标基因序列所需的最少变
# 化次数。如果无法实现目标变化，请返回 -1。 
# 
#  注意: 
# 
#  
#  起始基因序列默认是合法的，但是它并不一定会出现在基因库中。 
#  所有的目标基因序列必须是合法的。 
#  假定起始基因序列与目标基因序列是不一样的。 
#  
# 
#  示例 1: 
# 
#  
# start: "AACCGGTT"
# end:   "AACCGGTA"
# bank: ["AACCGGTA"]
# 
# 返回值: 1
#  
# 
#  示例 2: 
# 
#  
# start: "AACCGGTT"
# end:   "AAACGGTA"
# bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
# 
# 返回值: 2
#  
# 
#  示例 3: 
# 
#  
# start: "AAAAACCC"
# end:   "AACCCCCC"
# bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
# 
# 返回值: 3
#  
#  👍 45 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        """
        分析：
        1.每做一次变换，都需要去判断是否在基因库中，基因库里面的值是不重复的
        2.BFS广度优先搜索，左边出队，右边进队
        """
        posible = ['A', 'C', 'G', 'T']
        queue = [(start, 0)]
        while queue:
            (word, step) = queue.pop(0)
            if word == end:
                return step
            for i in range(len(word)):
                for p in posible:
                    temp = word[:i] + p + word[i+1:]
                    if temp in bank:
                        bank.remove(temp)  # 理解为层在缩小，即在第1个len(word)循环中，就把所有的可能性入队了
                        queue.append((temp, step + 1))
        return -1


if __name__ == '__main__':
    start = "AAAAACCC"
    str_li = list(start)
    str_li[0] = 'C'
    start = ''.join(str_li)
    print(str_li)
    print(start)
        
# leetcode submit region end(Prohibit modification and deletion)
