## 学习笔记

**初级搜索的优化方式：**不重复（fibonacci，数组存中间状态或者顺推），剪枝（生成括号问题），搜索方向（双向搜索，启发式搜索）

搜索问题，一定转换成状态树，数形结合

#### 剪枝

回溯算法或者是dfs中中，添加约束条件

#### 双向BFS

127.单词接龙

```python
import string
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList: return 0
        front = {beginWord}
        back = {endWord}
        dist = 1
        wordList = set(wordList)
        word_len = len(beginWord)
        while front:
            dist += 1
            next_front = set()
            for word in front:
                for i in range(word_len):
                    for c in string.ascii_letters:
                        if c != word[i]:
                            new_word = word[:i] + c + word[i + 1:]
                            if new_word in back:
                                return dist
                            if new_word in wordList:
                                next_front.add(new_word)
                                wordList.remove(new_word)
            front = next_front
            if len(back) < len(front):
                front, back = back, front
        return 0
```



#### 启发式搜索 A*Search

是基于BFS的

```python
def AstartSearch(graph, start, end):
    pq = collections.priority_queue() # 优先级 -> 估价函数
    pq.append([start])
    visited.add(start)
    while pq:
        node = pq.pop()  # 这一步更加智能一点？
        visited.add(node)
        process(node)
        nodes = generate_related_nodes(node)
        unvisited = [node for node in nodes if node not in visited]
        pq.push(unvisited)
```

**估价函数**

启发式函数：h(n)，用来评价哪些结点最有希望的是一个我们要找的结点，是一种告知搜索方向的方法，提供了一种明智的方法来猜测哪个邻居结点会导向一个目标

#### 回溯

回溯实际就是递归和分治，只是可以不断试错和回退

#### 位运算

| 含义                      | 位运算符（二进制） | 逻辑运算符（python） |      |
| ------------------------- | ------------------ | -------------------- | ---- |
| 按位或，一真为真          | \|                 | or                   |      |
| 按位与，一假为假          | &                  | and                  |      |
| 按位取反，假是真，真是假  | ~                  | not                  |      |
| 按位异或，相同为零不同为1 | ^                  |                      |      |
| 右移                      | >>                 |                      |      |
| 左移                      | <<                 |                      |      |

- 判断奇偶，与运算&，判断二进制最后一位是0还是1

```python
x % 2 == 1 ——> x & 1 == 1
x % 2 == 0 ——> x & 1 == 0
```

- x 除 2，右移一位，>>

```python
x = x / 2 ——> x = x >> 1, x >>= 1
mid = (left + right) / 2 ——> mid = (left + right) >> 1
```

- 清零最低位的1，把最低位的1变成0

```python
x = x & (x - 1), x &= x-1
```

- 得到最低位的1

```
x & -x 
```

- 将x清零

```
x & ~x
```

