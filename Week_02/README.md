## 学习笔记

[TOC]



#### 二叉树

#### 二叉查找树

##### 时间复杂度分析

查找、插入、删除跟树的高度成正比

- 退化成链表:o(n)
- 完全二叉树:o(logn)

#### 红黑树

#### 堆和堆排序

##### 1.定义

- 完全二叉树：除了最后一层，其他层的节点个数都是满的，最后一层的节点都靠左排列
- 堆中每一个节点的值都必须大于等于其子树中每个节点的值

##### 2.堆实现

- 数组存储
- 支持插入一个元素、删除堆顶元素（自底向上的思想)

##### 3.堆排序实现

- 建堆
- 排序

#### 图

##### 概念

有向图：微博

无向图：朋友圈

带权图、顶点、边

度：一个顶点有几条边

入度、出度

##### 存储方法

邻接矩阵、邻接表。

- 邻接居正存储方法的缺点是比较浪费空间，优点是查询效率高，方便矩阵运算

- 邻接表存储方法中每个顶点都对应一个链表，存储与其相连接的其他顶点，查询效率没有邻接矩阵高，但可以把链表换成更加高效的动态数据结构，平衡二叉树、跳表、散列表等

  

