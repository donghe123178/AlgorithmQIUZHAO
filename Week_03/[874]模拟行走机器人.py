# 机器人在一个无限大小的网格上行走，从点 (0, 0) 处开始出发，面向北方。该机器人可以接收以下三种类型的命令： 
# 
#  
#  -2：向左转 90 度 
#  -1：向右转 90 度 
#  1 <= x <= 9：向前移动 x 个单位长度 
#  
# 
#  在网格上有一些格子被视为障碍物。 
# 
#  第 i 个障碍物位于网格点 (obstacles[i][0], obstacles[i][1]) 
# 
#  机器人无法走到障碍物上，它将会停留在障碍物的前一个网格方块上，但仍然可以继续该路线的其余部分。 
# 
#  返回从原点到机器人所有经过的路径点（坐标为整数）的最大欧式距离的平方。 
# 
#  
# 
#  示例 1： 
# 
#  输入: commands = [4,-1,3], obstacles = []
# 输出: 25
# 解释: 机器人将会到达 (3, 4)
#  
# 
#  示例 2： 
# 
#  输入: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
# 输出: 65
# 解释: 机器人在左转走到 (1, 8) 之前将被困在 (1, 4) 处
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= commands.length <= 10000 
#  0 <= obstacles.length <= 10000 
#  -30000 <= obstacle[i][0] <= 30000 
#  -30000 <= obstacle[i][1] <= 30000 
#  答案保证小于 2 ^ 31 
#  
#  Related Topics 贪心算法 
#  👍 104 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        """
        想象xy坐标轴，有四个象限
        1.确定机器人所在方向，顺时针看，北东南西，用 0， 1， 2， 3 表示，
            向右转 i + 1, if = 4, 则 i = 0，用 i % 4 表示
            向左转 i - 1, if = -1, 则 i = 3，k[3] = k[-1], 不用处理
        2.机器人行走表示：从（0，0）开始，向北，东，南，西走，k = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        3.障碍物处理，用集合存储，值唯一不重复，例如{(1, 3), (2, 4)}
        4.记录机器人的当前坐标（x，y）,返回max(x^2 + y^2)
        """
        obstacle = set(map(tuple, obstacles))  # 集合，里面的元素是元组形式
        k = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        i = 0
        o = (0, 0)
        distance = 0
        for command in commands:
            if command == -1:
                i += 1
            elif command == -2:
                i -= 1
            else:
                for step in range(command):
                    tmp = (o[0] + k[i % 4][0], o[1] + k[i % 4][1])
                    if tmp in obstacle:
                        break
                    else:
                        o = tmp
                distance = max(distance, o[0] ** 2 + o[1] ** 2)
        return distance

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    obstacles = [[2, 4], [1, 3], [2, 4]]
    # map(function, iterable)，对序列中的每个元素都运用function这个函数，返回一个迭代器
    l = list(map(tuple, obstacles))  # {(1, 3), (2, 4)}
    # k = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # i = 0
    # o = (0, 0)
    # b = list(zip(o, k[i % 4], (1, 1)))   # [(0, 0, 1), (0, 1, 1)]
    # h = [x + y * z for x, y, z in zip(o, k[i % 4], (1, 1))]  # [0, 1]
    print(l)
    # print(b)
    # print(h)
