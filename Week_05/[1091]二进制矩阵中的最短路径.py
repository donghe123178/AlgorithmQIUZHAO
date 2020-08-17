# 在一个 N × N 的方形网格中，每个单元格有两种状态：空（0）或者阻塞（1）。 
# 
#  一条从左上角到右下角、长度为 k 的畅通路径，由满足下述条件的单元格 C_1, C_2, ..., C_k 组成： 
# 
#  
#  相邻单元格 C_i 和 C_{i+1} 在八个方向之一上连通（此时，C_i 和 C_{i+1} 不同且共享边或角） 
#  C_1 位于 (0, 0)（即，值为 grid[0][0]） 
#  C_k 位于 (N-1, N-1)（即，值为 grid[N-1][N-1]） 
#  如果 C_i 位于 (r, c)，则 grid[r][c] 为空（即，grid[r][c] == 0） 
#  
# 
#  返回这条从左上角到右下角的最短畅通路径的长度。如果不存在这样的路径，返回 -1 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[[0,1],[1,0]]
# 
# 输出：2
# 
#  
# 
#  示例 2： 
# 
#  输入：[[0,0,0],[1,1,0],[1,1,0]]
# 
# 输出：4
# 
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= grid.length == grid[0].length <= 100 
#  grid[i][j] 为 0 或 1 
#  
#  Related Topics 广度优先搜索 
#  👍 58 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # queue, n = [(0, 0, 2)], len(grid)
        # if grid[0][0] or grid[-1][-1]:  # 左上角和右下角有障碍物
        #     return -1
        # elif n <= 2:
        #     return n
        # for i, j, d in queue:
        #     for x, y in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1),
        #                  (i, j + 1), (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]:
        #         if 0 <= x < n and 0 <= y < n and not grid[x][y]:
        #             if x == n - 1 and y == n-1:
        #                 return d
        #             queue += [(x, y, d + 1)]
        #             grid[x][y] = 1
        # return -1

        """
        标准的BFS,枝丫是什么，走的方向，8个方向
        备忘录，用于记录已经访问的位置
        """
        if not grid or grid[0][0] or grid[-1][-1]:
            return -1
        n = len(grid)
        if n <= 2:
            return n
        moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        queue = [(0, 0, 1)]
        grid[0][0] = 1
        while queue:
            i, j, step = queue.pop(0)
            for dx, dy in moves:
                x, y = i + dx, j + dy
                if x == n - 1 and y == n - 1:
                    return step + 1
                if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                    queue.append((x, y, step + 1))
                    grid[x][y] = 1
        return -1

# leetcode submit region end(Prohibit modification and deletion)
