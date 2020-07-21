# 给定一个二叉树，返回它的中序 遍历。 
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
# 输出: [1,3,2] 
# 
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？ 
#  Related Topics 栈 树 哈希表 
#  👍 585 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        """
        1.递归，
        时间复杂度：O(N)
        空间复杂度：O(N)
        """
        # 1.递归简洁写法
        # if not root:
        #     return []
        # return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

        # 第二种写法
        # def dfs(root):
        #     if not root:
        #         return None
        #     dfs(root.left)
        #     res.append(root.val)
        #     dfs(root.right)
        # res = []
        # dfs(root)
        # return res
        """
        [二叉树的遍历](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/solution/tu-jie-er-cha-shu-de-si-chong-bian-li-by-z1m/)
        2.迭代。递归是自动调用栈来保存每个函数的调用，迭代就是用栈来显示模拟这个过程
        栈的特点：后进先出，我们可以决定在什么时候触发弹出机制
        时间复杂度，空间复杂度为O(n)
        """
        # res = []
        # stack = []
        # while stack or root:
        #     if root:
        #         stack.append(root)
        #         root = root.left
        #     else:
        #         tmp = stack.pop()
        #         res.append(tmp.val)
        #         root = tmp.right
        # return res
# leetcode submit region end(Prohibit modification and deletion)
