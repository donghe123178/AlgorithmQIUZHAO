# 您需要在二叉树的每一行中找到最大的值。 
# 
#  示例： 
# 
#  
# 输入: 
# 
#           1
#          / \
#         3   2
#        / \   \  
#       5   3   9 
# 
# 输出: [1, 3, 9]
#  
#  Related Topics 树 深度优先搜索 广度优先搜索 
#  👍 82 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        """
        BFS,广度优先搜索
        """
        res, queue = [], [root]
        while queue:
            max_value = float('-inf')
            for i in range(len(queue)):  # 表示当前层的个数
                cur = queue.pop(0)
                if not cur:
                    continue
                max_value = max(max_value, cur.val)
                queue.append(cur.left)  # 没有分开判断，则可能有一子树为空，也添加进来
                queue.append(cur.right)
            if max_value != float('-inf'): # 原因在于为空时，[],如果没有添加此句，会将inf田间进来
                res.append(max_value)
        return res

        # if not root:
        #     return []
        # res, queue = [], [root]
        # while queue:
        #     curr_max = float('-inf')
        #     for _ in range(len(queue)):
        #         node = queue.pop(0)
        #         curr_max = max(curr_max, node.val)
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #     res.append(curr_max)
        # return res
        
# leetcode submit region end(Prohibit modification and deletion)
