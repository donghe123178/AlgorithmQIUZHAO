# 给定一个二叉树，返回它的 前序 遍历。 
# 
#  示例: 
# 
#  输入: [1,null,2,3]  
#    1
#     \
#      2
#     /
#    3 
# 
# 输出: [1,2,3]
#  
# 
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？ 
#  Related Topics 栈 树 
#  👍 313 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # if not root:
        #     return []
        # return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

        # 递归第二种方法
        # def dfs(root):
        #     if not root:
        #         return None
        #     if root:
        #         res.append(root.val)
        #         dfs(root.left)
        #         dfs(root.right)
        # res =[]
        # dfs(root)
        # return res

        # 迭代，思想就是直接把当前非叶子节点从栈顶弹出，然后将子节点进栈
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            tmp = stack.pop()
            res.append(tmp.val)
            if tmp.right:
                stack.append(tmp.right)
            if tmp.left:
                stack.append(tmp.left)
        return res

# leetcode submit region end(Prohibit modification and deletion)
