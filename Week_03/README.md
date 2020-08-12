## 学习笔记

#### 递归、分治、回溯

**思维要点**：

1.不要人肉递归

2.找最近重复性子问题

3.数学归纳法思维

##### 递归recursion

```python
def recursion(lever, param1, param2,...):
    # 递归终结条件
    if level > max_level:
        precess_result
        return 
    # 处理当前层逻辑
    process(level, data...)
    # 下探到下一层
    self.recursion(level+1, p1,...)
    # 清理当前层的状态
```

##### **分治**

自上而下分解，自下而上合并

关键点：怎样拆成子问题，怎么合并子结果，怎么做质量保证

```python
def divide_conquer(problem, param1, param2,...):
    # 递归终止
    if problem is None:
        print_result
        return 
    # 准备数据
    data = prepare_data(problem)
    subproblems = split_problem(problem, data)
    # 分治子问题
    subresult1 = self.divide_conquer(subproblems[0], p1,...)
    subresult2 = self.divide_conquer(subproblems[1], p2,...)
    ...
    # 合并结果
    result = process_result(subresult1, subresult2,...)
    # 清理当前层状态
```

#### **回溯**

回溯法是一个剪了枝的二叉树

##### 判断回溯

一个问题，感觉不穷举一下就没法知道答案，那就可以开始回溯了

常见的回溯问题类型：

- 有没有解
- 求所有解：所有解的个数，所有解的具体信息
- 求最优解

不断地去每一层去试就好了，常用两个变量，**res保存最终结果，path保存已经走过的路径**

```python
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        """
        分析：
        想象成有2*n个格子，每个格子既可以插入左括号，又可以插入右括号，二叉树结构，n层
        1.插入括号的数量<=n
        2.可以插入右括号的前提是 剩下的左括号数量 < 右括号，说明放入的左括号>右括号
        DFS
        """
        res = []
        self.dfs(res, n, n, '')
        return res

    def dfs(self, res, left, right, path):
        if left == 0 and right == 0:
            res.append(path)
            return
        if left > 0:
            self.dfs(res, left - 1, right, path + '(')
        if left < right:
            self.dfs(res, left, right - 1, path + ')')
     
    def dfs(self, res, left, right, path):
        if left == 0 and right == 0:
            res.append(path)
            return
        if left < 0:
            return
        if left > right:
            return
        self.dfs(res, left - 1, right, path + '(')
        self.dfs(res, left, right - 1, path + ')')
```



#### 搜索—Search

搜索——遍历

- 每个节点都要访问一次
- 每个节点仅仅访问一次
- 节点的访问顺序不同：深度优先，广度优先，优先级优先
- 二叉树，多叉树

##### 深度优先搜索

DFS:Depth first search

**遍历顺序**——根节点是最先开始访问的，然后左子树访问到底，右子树访问到底

```python
# 遍历顺序：根节点，左子树，右子树
# 1.递归写法-多叉树
visited = set()
def dfs(node, visited):
    # terminator
    if node in visited:
        return 
    visited.add(node)
    # process current node here
    for next_node in node.children:
        if not next_node in visited:
            dfs(next_node, visited)
# 2.递归写法-二叉树
visited = set()
def dfs(node):
    if node in visited:
        return 
    visited.add(node)
    # process current node here
    dfs(node.left)
    dfs(node.right)           
            
# 2.非递归写法，手动维护一个栈，循环
def DFS(self, root):
    if root is None:
        return []
    visited, stack = [], [root]
    while stack:
        node = stack.pop() # 栈顶出
        visited.add(node)
        process(node)
        nodes = generate_related_nodes(node)
        stack.push(nodes) # 栈顶进
```

##### 广度优先搜索

BPS:Breadth first search

**遍历顺序**——一层一层地遍历下去，想象成一个水滴，从根节点开始，一层一层扩散下去，遍历结果是一个一维数组

**使用场景**——层序遍历（把二叉树分层，每一层从左到右遍历，**关键点**在于要求区分每一层，返回一个二维数组），最短路径

```python
# 用一个队列,先入先出，例如，一个二叉树[1,2,3,4,5,6]
# 不需要确定当前遍历到那一层
def BFS(root):
    visited, queue =[], [root]   
    while queue:  
        cur = queue.pop() # 队头出
        visited.add(start) 
        for node in cur:
            if node not in visited:
                queue.push(node) # 队尾进

# 确定当前遍历到那一层了
level = 0
while queue：
    size = len(queue)
    while size:
        cur = queue.pop()
        for node in cur:
            if node not in visited:
                queue.push(node) # 队尾进
        size -= 1    
    level += 1
                
# 用一个队列,先入先出，图
def BFS(graph, start, end):
    queue = []
    queue.append([start])  
    visited.add(start) 
    while queue: 
        node = queue.pop()
        visited.add(node) 
        process(node)
        nodes = generate_related_nodes(node)
        queue.push(nodes) 
```

贪心：当下做局部最优判断

回溯：能够回退

动态规划：最优判断+回退

#### 贪心算法—Greedy

##### 定义

在每一步选择中都采取在当前状态下最优的选择，从而希望全局最优

**特点**：对每个子问题的解决方案都做出选择，不能回退

##### 适用贪心算法的场景

解决最优化问题，问题能够分解成子问题来解决，子问题的最优解能递推到**最终问题的最优解**，最优子结构

贪心算法的切入点有的可能比较巧妙

##### 贪心算法与动态规划的不同：

贪心算法对每个子问题的解决方案都做出选择，不能回退，动态规划则会保存以前的运算结果，并根据以前的结果对当前进行回退，有回退功能

#### 二分查找

##### 二分查找的前提

- 单调性：目标函数单调递增或者递减，**有序**
- 存在上下界
- 能够通过索引访问，**数组**

##### 代码模板

```python
# 数组升序
left,right = 0, len(array) - 1
while left <= right:
	mid = (left + right) / 2
	if array[mid] == target:
		break or return result
	elif array[mid] < target:
        # 如果不是整数，直接等于mid即可
        left = mid + 1
    else:
        right = mid - 1
```

##### 关键点：

**确定返回条件**

**确定夹逼条件**

