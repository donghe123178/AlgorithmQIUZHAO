## 学习笔记

#### 动态规划

最优子结构，子问题间必须互相独立。常常是求有多少种方案，或者是最优方案

#### 动态规划DP步骤

- 1.找重复性子问题（分治思想）
- 2.定义状态数组：一维的还是二维的，数组的值代表的是什么意思
- 3.写出状态转移方程

##### 递归法：自顶向下

是从上向下延伸，都是从一个规模较大的原问题，向下逐渐分解规模，直到遇见base case，然后逐层返回答案

##### 递推法：自底向上（通常采用）

直接从最底下、最简单、最小问题规模开始往上推，直到推到我们想要的答案，这就是动态规划的思路，一般都脱离了递归，而是由循环迭代完成计算。

**空间优化**：二维变一维，一维变常量

#### 细节问题

关键点1：确定`dp[i]，dp[i][j]`代表什么意思，一般就是题目中所求的量，一维想象成**一行格子，二维想象成一张表**

关键点2：dp[i]与s[i]之间的对应关系，应该一一对应，还是dp[i+1]对应s[i]，即需不需要在外面套一层

关键点3：for 循环的时候应该从0开始，还是1开始，还是2开始

关键点4：写递推方程、状态转移方程：认真分析题目，找出限制条件，运用数学归纳法，还有就是多做题靠经验

```python
# 一维数组
dp = [0] * n 
dp = [0 for i in range(3)]
# 二维数组，里面n代表列，外层m代表行，生成dp[m][n]
dp = [[0 for col in range(3)] for row in range(2)]
dp = [[0] * n for _ in range(m)]
# 其他
dp = [i for i in range(3)] # [0, 1, 2]
```

打家劫舍

```python
# 从0开始循环，站在原数组角度
def rob(self, nums):
    n = len(nums)
    if n == 0:
        return 0
    dp = [0] * (n + 1)
    for k in range(n):
        dp[k+1] = max(dp[k], dp[k-1] + nums[k])
    return dp[n]
# 站在dp数组角度，循环至n+1结束
def rob(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """   
    n = len(nums)
    if n == 0:
        return 0
    dp = [0] * (n + 1)
    dp[1] = nums[0]
    for k in range(2, n+1):
        dp[k] = max(dp[k-1], dp[k-2] + nums[k-1])
    return dp[n]

```

参考文章

[详解动态规划](https://leetcode-cn.com/problems/coin-change/solution/dong-tai-gui-hua-tao-lu-xiang-jie-by-wei-lai-bu-ke/)