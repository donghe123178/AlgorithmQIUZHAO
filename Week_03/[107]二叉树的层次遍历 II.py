# 给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历） 
# 
#  例如： 
# 给定二叉树 [3,9,20,null,null,15,7], 
# 
#      3
#    / \
#   9  20
#     /  \
#    15   7
#  
# 
#  返回其自底向上的层次遍历为： 
# 
#  [
#   [15,7],
#   [9,20],
#   [3]
# ]
#  
#  Related Topics 树 广度优先搜索 
#  👍 280 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        """
        BFS，最后将结果反转一下
        """
        res, queue = [], [root]
        while queue:
            level = []
            for i in range(len(queue)):
                cur = queue.pop(0)
                if not cur:
                    continue
                level.append(cur.val)
                queue.append(cur.left)
                queue.append(cur.right)
            if level:
                res.append(level)
        return res[::-1]
# leetcode submit region end(Prohibit modification and deletion)
