# 给定一个 N 叉树，返回其节点值的后序遍历。 
# 
#  例如，给定一个 3叉树 : 
# 
#  
# 
#  
# 
#  
# 
#  返回其后序遍历: [5,6,3,2,4,1]. 
# 
#  
# 
#  说明: 递归法很简单，你可以使用迭代法完成此题吗? Related Topics 树 
#  👍 85 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        # 1.递归
        # if not root:
        #     return []
        # res = []
        # for child in root.children:
        #     res.extend(self.postorder(child))
        # res.append(root.val)
        # return res

        # 2.递归通用模板
        # def dfs(root):
        #     if not root:
        #         return None
        #     for child in root.children:
        #         dfs(child)
        #     res.append(root.val)
        # res = []
        # dfs(root)
        # return res

        # 3.迭代写法,时间复杂度空间复杂度O(M)
        if root is None:
            return []
        stack, res = [root], []
        while stack:
            root = stack.pop()
            if root is not None:
                res.append(root.val)
            for child in root.children:
                stack.append(child)
        return res[::-1]


        
# leetcode submit region end(Prohibit modification and deletion)
