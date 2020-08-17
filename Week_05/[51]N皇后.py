# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。 
# 
#  
# 
#  上图为 8 皇后问题的一种解法。 
# 
#  给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。 
# 
#  每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。 
# 
#  示例: 
# 
#  输入: 4
# 输出: [
#  [".Q..",  // 解法 1
#   "...Q",
#   "Q...",
#   "..Q."],
# 
#  ["..Q.",  // 解法 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# 解释: 4 皇后问题存在两个不同的解法。
#  
# 
#  
# 
#  提示： 
# 
#  
#  皇后，是国际象棋中的棋子，意味着国王的妻子。皇后只做一件事，那就是“吃子”。当她遇见可以吃的棋子时，就迅速冲上去吃掉棋子。当然，她横、竖、斜都可走一到七步
# ，可进可退。（引用自 百度百科 - 皇后 ） 
#  
#  Related Topics 回溯算法 
#  👍 499 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# class Solution(object):
#     def solveNQueens(self, n):
#         """
#         :type n: int
#         :rtype: List[List[str]]
#         """
#         """
#         回溯算法：想象成一棵决策树，每一层代表什么，决策树的高度代表什么
#         每一层代表棋盘上的每一行，每个节点可以做出的选择是，在该行的任意一列放置一个皇后
#         放置的条件是：
#         该列不能有皇后，右上方不能有皇后，左上方不能有皇后
#         时间复杂度是O(N!)
#         空间复杂度是O(N^2)
#         """
#         self.n = n
#         self.res = []
#         # board = [['.' for i in range(n)] for _ in range(n)]
#         board = [['.'] * n for _ in range(n)]  # 初始化棋盘，一个二维数组，观察，输出结果推导出来的
#         self.backtrace(board, 0)
#         return self.res
#
#     def isvalid(self, board, row, col):  # 判断哪里可以做选择，哪里不可以做选择
#         for i in range(row):
#             if board[i][col] == 'Q':
#                 return False
#         i, j = row - 1, col + 1
#         while i >= 0 and j < self.n:
#             if board[i][j] == 'Q':
#                 return False
#             i -= 1
#             j += 1
#         i, j = row - 1, col - 1
#         while i >= 0 and j >= 0:
#             if board[i][j] == 'Q':
#                 return False
#             i -= 1
#             j -= 1
#         return True
#
#     def backtrace(self, board, row):  # board是路径，存储做过的选择，选择列表:第row行所有的列
#         if row == self.n:   # 递归终止条件：遍历完棋盘的行数
#             temp = []  # 存储一种解法
#             for s in board:
#                 temp.append(''.join(s))  # 将列表，转换成字符串存储在一个列表中
#             self.res.append(temp)  # 收集解法
#             return
#         for col in range(self.n):
#             if self.isvalid(board, row, col):
#                 board[row][col] = 'Q'  # 做出选择
#                 self.backtrace(board, row + 1)
#                 board[row][col] = '.'  # 回退，撤销选择

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        # 位运算
        if n < 1: return []
        self.count = 0
        self.DFS(n, 0, 0, 0, 0)
        return self.count

    def DFS(self, n, row, cols, pie, na):
        if row >= n:
            self.count += 1
            return
        bits = (~(cols | pie | na)) & ((1 << n) - 1)
        while bits:
            p = bits & -bits  # 得到最低位的1
            bits = bits & (bits - 1)  # 把最低位的1变为0，在p位置上放入皇后
            self.DFS(n, row + 1, cols | p, (pie | p) << 1, (na | p) >> 1)


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        """
        回溯算法
        时间复杂度：O(N!)
        空间复杂度：O(N*N)
        """

        def dfs(queens, pie, na):  # queens里面记录的是每一行皇后所处的位置
            p = len(queens)
            if p == n:  # 行数，决策树的深度等于行数
                res.append(queens)
                return
            for q in range(n):  # 决策数的分支，列数
                if q not in queens and p - q not in pie and p + q not in na:  # 约束条件，用于剪枝
                    dfs(queens + [q], pie + [p - q], na + [p + q])

        res = []
        dfs([], [], [])
        print(res)
        return [['.' * i + 'Q' + '.' * (n - i - 1) for i in sol] for sol in res]


if __name__ == '__main__':
    # board = [['.' for i in range(3)] for _ in range(3)]  # 初始化一个棋盘，生成的每列是字符串
    # # 将棋盘降成一维，新第一列，代表原棋盘的第一行
    # for s in board:  # 棋盘的行
    #     new = ''.join(s)
    #     print(new)
    # boar = [['.' * 3] for _ in range(3)]  # 生成的列是连在一起的字符串，不能修改
    # print(board)
    # print(boar)
    s = Solution()
    b = s.solveNQueens(4)
    print(b)

# leetcode submit region end(Prohibit modification and deletion)
