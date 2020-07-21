# 给定一个二叉树，返回它的 后序 遍历。 
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
# 输出: [3,2,1] 
# 
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？ 
#  Related Topics 栈 树 
#  👍 350 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # if not root:
        #     return []
        # return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) +[root.val]

        # def dfs(root):
        #     if not root:
        #         return None
        #     dfs(root.left)
        #     dfs(root.right)
        #     res.append(root.val)
        # res = []
        # dfs(root)
        # return res

        # 按照根，右，左的顺序弹出，最后将结果反向输出
        # 时间复杂度，空间复杂度O(n)
        # if not root:
        #     return []
        # res, stack, cur = [], [], root
        # while stack or cur:
        #      while cur:
        #         res.append(cur.val)
        #         stack.append(cur)
        #         cur = cur.right
        #      tmp = stack.pop()
        #      cur = tmp.left
        # return res[::-1]

        # 另一种写法，广度优先搜索，从根节点开始迭代，弹出栈顶元素输出到列表种，然后依次按照从上到下、从左至右的顺序依次压入栈中
        # 深度优先搜索后序遍历：从下到上，从左至右
        # if root is None:
        #     return []
        # stack = [root]
        # res = []
        # while stack:
        #     root = stack.pop()
        #     res.append(root.val)
        #     if root.left is not None:
        #         stack.append(root.left)
        #     if root.right is not None:
        #         stack.append(root.right)
        # return res[::-1]

        # 完全模拟递归过程：后序遍历需要先输出子节点再输出父节点，如果当前节点不是叶子节点就不能弹出
        # 思路，用一个标记，只有已经遍历过的节点才可以弹出
        if not root:
            return []
        stack = [(0, root)]
        res = []
        while stack:
            flag, node = stack.pop()
            # if not node:
            #     continue
            if flag == 1:
                res.append(node.val)
            else:
                stack.append((1, node))
                stack.append((0, root.right))
                stack.append((0, root.left))
        return res

# leetcode submit region end(Prohibit modification and deletion)
