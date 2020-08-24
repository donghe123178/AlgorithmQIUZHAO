# 给出一个区间的集合，请合并所有重叠的区间。 
# 
#  
# 
#  示例 1: 
# 
#  输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
#  
# 
#  示例 2: 
# 
#  输入: intervals = [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。 
# 
#  注意：输入类型已于2019年4月15日更改。 请重置默认代码定义以获取新方法签名。 
# 
#  
# 
#  提示： 
# 
#  
#  intervals[i][0] <= intervals[i][1] 
#  
#  Related Topics 排序 数组 
#  👍 562 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # 排序，按第一列
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        i = 0
        for temp in intervals[1:]:
            if res[i][1] < temp[0]:
                res.append(temp)
                i += 1
            elif temp[0] <= res[i][1] <= temp[1]:
                res[i] = [res[i][0], temp[1]]
        return res
if __name__ == '__main__':
    s = Solution()
    s.merge([[1,4],[2,3]])

# leetcode submit region end(Prohibit modification and deletion)
