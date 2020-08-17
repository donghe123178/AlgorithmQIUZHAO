# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。 
# 
#  每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？ 
# 
#  注意：给定 n 是一个正整数。 
# 
#  示例 1： 
# 
#  输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶 
# 
#  示例 2： 
# 
#  输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶
#  
#  Related Topics 动态规划 
#  👍 1176 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        1.递归，斐波拉契数列
        时间复杂度：O(2^N)，指数级别
        空间复杂度：O(N)，调用栈的深度是楼梯数
        """
        # if n <= 2:
        #     return n
        # return self.climbStairs(n-1) + self.climbStairs(n-2)

        """
        2.动态递推，用一个数组把中间结果给存储下来
        时间复杂度，空间复杂度都是O(N)
        """
        # dp = [0] * (n+1)  # 状态数组
        # for i in range(n+1):
        #     if i <= 2:  # base case
        #         dp[i] = i
        #     else:
        #         dp[i] = dp[i-2] + dp[i-1]  # 递推方程
        # return dp[n]

        """
        2.改进,不需要把每一个状态都记录下来，空间降维
        时间复杂度：O(N)，空间复杂度位O(1)
        """
        # re, p, q =0, 1, 2
        # for i in range(n + 1):
        #     if i <= 2:
        #         re = i
        #     else:
        #         re = p + q
        #         p, q = q, re
        # return re

        """
        3.拓展1：可以走1，2，3步，变成零钱兑换问题
        问题1：一共有多少种走法，用一列表记录路径，回溯
        问题2：打印出方法：状态数的路径
        问题3：相邻两步的步伐不能相同，剪枝
        """
        steps = [1, 2, 3]
        res = []

        def dfs(n, tmp):
            if n == 0:
                res.append(tmp[:])
                print(tmp)  # 打印
                return

            for step in steps:
                if n < step or (tmp and step == tmp[-1]):  # 约束条件，剪枝
                    continue
                else:
                    tmp += [step]
                    dfs(n - step, tmp)
                    tmp.pop()  # 清理当前层状态

        dfs(n, [])
        return len(res)


if __name__ == '__main__':
    a = Solution()
    b = a.climbStairs(3)
    print(b)

# leetcode submit region end(Prohibit modification and deletion)
