# 给定一个 N 叉树，返回其节点值的前序遍历。 
# 
#  例如，给定一个 3叉树 : 
# 
#  
# 
#  
# 
#  
# 
#  返回其前序遍历: [1,3,5,6,2,4]。 
# 
#  
# 
#  说明: 递归法很简单，你可以使用迭代法完成此题吗? Related Topics 树 
#  👍 89 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        # 1.简洁递归
        # if not root:
        #     return []
        # res = [root.val]
        # for node in root.children:
        #     res.extend(self.preorder(node))
        # return res

        # 2.通用模板递归法
        def dfs(root):
            if not root:
                return None
            res.append(root.val)
            for child in root.children:
                dfs(child)
        res = []
        dfs(root)
        return res

        # 3.迭代方法
        # if not root:
        #     return []
        # stack, res = [root], []
        # while stack:
        #     root = stack.pop()
        #     res.append(root.val)
        #     stack.extend(root.children[::-1])
        # return res


        
# leetcode submit region end(Prohibit modification and deletion)
