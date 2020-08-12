# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。 
# 
#  
# 
#  示例： 
# 二叉树：[3,9,20,null,null,15,7], 
# 
#      3
#    / \
#   9  20
#     /  \
#    15   7
#  
# 
#  返回其层次遍历结果： 
# 
#  [
#   [3],
#   [9,20],
#   [15,7]
# ]
#  
#  Related Topics 树 广度优先搜索 
#  👍 592 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        """
        分析：本题关键点就在于要区分每一层，并将每一层都要归结在一起
        BFS:广度优先搜索，用队列，左边出，右边进
            用一个列表类型的变量level记录当前层，并获取其长度属性值，
            确保每一层都是空队列来，进行入队出队操作后，空队列走
        """
        # 用队列
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
        return res

        # 用双端队列
        # res, queue =[], deque()
        # queue.append(root)
        # while queue:
        #     level = []
        #     size = len(queue)
        #     for i in range(size):
        #         cur = queue.popleft()
        #         if not cur:
        #             continue
        #         level.append(cur.val)
        #         queue.append(cur.left)
        #         queue.append(cur.right)
        #     if level:
        #         res.append(level)
        # return res

        """
        DFS:深度优先搜索，用递归
        每下探一层，都要记录当前在哪一层，用变量level记录楼层号，并创建楼层，即添加列表
        """
    #     res = []
    #     self.dfs(root, 0, res)
    #     return res
    #
    # def dfs(self, root, level, res):
    #     if not root:
    #         return
    #     if len(res) == level:
    #         res.append([])
    #     res[level].append(root.val)
    #     self.dfs(root.left, level + 1, res)
    #     self.dfs(root.right, level + 1, res)

# leetcode submit region end(Prohibit modification and deletion)
