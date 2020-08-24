## 布隆过滤器和LRU Cache

[TOC]

#### 一、布隆过滤器的实现及应用

##### 1. 应用背景

比特币网络、分布式系统、Redis缓存、垃圾邮件过滤、评论的过滤等场景中，如何判断一个元素是否存在一个集合中，且不会占用很大的内存空间？——**Bloom Filter**

##### 2. 实现原理

- 一个很长的**二进制向量（位数组）**
- 一系列**随机映射函数**
- 空间效率和查询时间远远超过一般的算法
- 有一定误判率和删除困难

与**哈希表+拉链存储重复元素**的方案相比，布隆过滤器只存**在不在（二进制位是不是1）**的信息，所需内存空间很少

##### 3. 添加元素

将要添加的元素给K个哈希函数，计算出对应于二进制位数组上的k个位置，将这k个位置设位1

##### 4. 查询元素

将要查询的元素给k个哈希函数，得到对应于位数组上的k个位置

- 如果k个位置有一个为0，则肯定不在集合中
- 如果k个位置全部为1，则可能在集合中

##### 5. Python实现

```python
from bitarray import bitarray 
import mmh3 
class BloomFilter: 
	def __init__(self, size, hash_num):  # 二进制向量大小，哈希函数个数
		self.size = size 
		self.hash_num = hash_num 
		self.bit_array = bitarray(size) 
		self.bit_array.setall(0) 
	def add(self, s): # 添加
		for seed in range(self.hash_num): 
			result = mmh3.hash(s, seed) % self.size 
			self.bit_array[result] = 1 
	def lookup(self, s): # 查询
		for seed in range(self.hash_num): 
			result = mmh3.hash(s, seed) % self.size 
			if self.bit_array[result] == 0: 
				return "Nope" 
		return "Probably" 
bf = BloomFilter(500000, 7) 
bf.add("dantezhao") 
print (bf.lookup("dantezhao")) 
print (bf.lookup("yyj")) 
```

#### 二、LRU Cache的实现、应用和题解

##### 1.应用背景

- cpu的高速缓存

##### 2.实现原理

**哈希表+双向链表**，O(1)查询，修改，更新

**两个要素**：缓存大小，替换策略：最近最少使用的放在最后去淘汰

注：本文用哈希表记录元素的位置，双向链表头部存储最新访问的元素，尾部记录以前访问需要最先淘汰的元素

##### 3.获取数据

根据传入的key去哈希表里拿到对应的元素，如果该元素存在，则把元素挪到链表的头部，表示最新访问的

##### 4.写入数据

首先判断key是否在哈希表里，如果存在就更新值，并把元素挪到链表的头部，表示这是最新访问的，如果不存在，说明这是一个新元素，此时需要判断cache容量，如果不够，则需要淘汰链表末尾元素，再将新的元素插入链表头部，如果够，就直接再链表头部追加新的元素。

##### 5.python实现

###### 5.1 使用有序字典

```python
import collections
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dic = collections.OrderedDict()
        self.remain = capacity

    # 获取数据，两种情况
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dic:
            return -1
        v = self.dic.pop(key)
        self.dic[key] = v  # key作为最新访问的
        return v

    # 写入数据，两种情况
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dic:
            self.dic.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:
                self.dic.popitem(last=False) # 先进先出，删除最先被添加的，即最久没被访问的
        self.dic[key] = value
```

###### 5.2 手写双向链表

```python
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        # 新建两个节点 head 和 tail
        self.head = ListNode()
        self.tail = ListNode()
        # 初始化链表为 head <-> tail
        self.head.next = self.tail
        self.tail.prev = self.head

    # 因为get与put操作都可能需要将双向链表中的某个节点移到末尾，所以定义一个方法
    def move_node_to_tail(self, key):
            # 先将哈希表key指向的节点拎出来，为了简洁起名node
            #      hashmap[key]                               hashmap[key]
            #           |                                          |
            #           V              -->                         V
            # prev <-> node <-> next         pre <-> next   ...   node
            node = self.hashmap[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            # 之后将node插入到尾节点前
            #                 hashmap[key]                 hashmap[key]
            #                      |                            |
            #                      V        -->                 V
            # prev <-> tail  ...  node                prev <-> node <-> tail
            node.prev = self.tail.prev
            node.next = self.tail
            self.tail.prev.next = node
            self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.hashmap:
            # 如果已经在链表中了久把它移到末尾（变成最新访问的）
            self.move_node_to_tail(key)
        res = self.hashmap.get(key, -1)
        if res == -1:
            return res
        else:
            return res.value

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            # 如果key本身已经在哈希表中了就不需要在链表中加入新的节点
            # 但是需要更新字典该值对应节点的value
            self.hashmap[key].value = value
            # 之后将该节点移到末尾
            self.move_node_to_tail(key)
        else:
            if len(self.hashmap) == self.capacity:
                # 去掉哈希表对应项
                self.hashmap.pop(self.head.next.key)
                # 去掉最久没有被访问过的节点，即头节点之后的节点
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
            # 如果不在的话就插入到尾节点前
            new = ListNode(key, value)
            self.hashmap[key] = new
            new.prev = self.tail.prev
            new.next = self.tail
            self.tail.prev.next = new
            self.tail.prev = new
```

参考文章：

[1]https://www.cnblogs.com/cpselvis/p/6265825.html

[2]https://leetcode-cn.com/problems/lru-cache/solution/shu-ju-jie-gou-fen-xi-python-ha-xi-shuang-xiang-li/