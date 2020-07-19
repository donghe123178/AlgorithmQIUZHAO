# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。 
# 
#  求在该柱状图中，能够勾勒出来的矩形的最大面积。 
# 
#  
# 
#  
# 
#  以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。 
# 
#  
# 
#  
# 
#  图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。 
# 
#  
# 
#  示例: 
# 
#  输入: [2,1,5,6,2,3]
# 输出: 10 
#  Related Topics 栈 数组 
#  👍 803 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        """
        1.暴力法，找到每一根柱子所能构建的最大面积，这时高度固定，找出最大宽度
        最大宽度的左右边界确定：向左右探测，第一次比当前柱子矮的位置
        用一个max_area记录当前的最大面积
        时间复杂度为O(N^2)
        """
        # area = 0
        # for i in range(0, len(heights)):
        #     left = i
        #     right = i
        #     while left >= 0 and heights[left] >= heights[i]:
        #         left -= 1
        #     while right < len(heights) and heights[right] >= heights[i]:
        #         right += 1
        #     area = max(area, heights[i] * (right - left - 1))
        # return area

        """
        2.维护一个单调递增的栈
        时间复杂度为O(n),空间复杂度为O(n)
        """
        stack = []
        heights = [0] + heights + [0]
        area = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                tmp = stack.pop()
                area = max(area, (i - stack[-1] - 1) * heights[tmp])
            stack.append(i)
        return area
# leetcode submit region end(Prohibit modification and deletion)
