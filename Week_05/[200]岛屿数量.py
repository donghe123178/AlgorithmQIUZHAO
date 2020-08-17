# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。 
# 
#  岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。 
# 
#  此外，你可以假设该网格的四条边均被水包围。 
# 
#  
# 
#  示例 1: 
# 
#  输入:
# [
# ['1','1','1','1','0'],
# ['1','1','0','1','0'],
# ['1','1','0','0','0'],
# ['0','0','0','0','0']
# ]
# 输出: 1
#  
# 
#  示例 2: 
# 
#  输入:
# [
# ['1','1','0','0','0'],
# ['1','1','0','0','0'],
# ['0','0','1','0','0'],
# ['0','0','0','1','1']
# ]
# 输出: 3
# 解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集 
#  👍 704 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        """
        分析：从一个点扩散开，找到其连通的点。
        如何扩散，想象成一个平面，xy轴，原点，跟模拟机器人行走像，顺指针
        从陆地1开始，找到所有与之相连的1，并标记，形成一个岛屿
        1. BFS,队列，所有加入队列的点（为1才加入），马上被标记
        是对每一个格子做DFS,队列 经历1次 空-有-空，岛屿数量就加+1
        """
        # m = len(grid)
        # if m == 0:
        #     return 0
        # n = len(grid[0])
        # marked = [[False for _ in range(n)] for _ in range(m)]
        # count = 0
        # directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # for i in range(m):
        #     for j in range(n):
        #         if not marked[i][j] and grid[i][j] == '1':
        #             queue = []
        #             queue.append((i, j))
        #             marked[i][j] = True
        #             while queue:
        #                 cur_x, cur_y = queue.pop(0)
        #                 for k in directions:
        #                     new_i = cur_x + k[0]
        #                     new_j = cur_y + k[1]
        #                     if  0 <= new_i < m and 0 <= new_j < n and not marked[new_i][new_j] and grid[new_i][new_j] == '1':
        #                         queue.append((new_i, new_j))
        #                         marked[new_i][new_j] = True
        #             count += 1
        # return count


        """
        DFS，递归法
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        marked = [[False for _ in range(n)] for _ in range(m)]
        count = 0
        # 从第 1 行、第 1 格开始，对每一格尝试进行一次 DFS 操作
        for i in range(m):
            for j in range(n):
                # 只要是陆地，且没有被访问过的，就可以使用 DFS 发现与之相连的陆地，并进行标记
                if not marked[i][j] and grid[i][j] == '1':
                    # count 可以理解为连通分量，你可以在深度优先遍历完成以后，再计数，
                    # 即这行代码放在【位置 1】也是可以的
                    self.__dfs(grid, i, j, m, n, marked)
                    count += 1
        return count

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def __dfs(self, grid, i, j, m, n, marked):
        marked[i][j] = True
        for direction in self.directions:
            new_i = i + direction[0]
            new_j = j + direction[1]
            if 0 <= new_i < m and 0 <= new_j < n and not marked[new_i][new_j] and grid[new_i][new_j] == '1':
                self.__dfs(grid, new_i, new_j, m, n, marked)

# leetcode submit region end(Prohibit modification and deletion)
