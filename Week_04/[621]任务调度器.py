# 给定一个用字符数组表示的 CPU 需要执行的任务列表。其中包含使用大写的 A - Z 字母表示的26 种不同种类的任务。任务可以以任意顺序执行，并且每个任务
# 都可以在 1 个单位时间内执行完。CPU 在任何一个单位时间内都可以执行一个任务，或者在待命状态。 
# 
#  然而，两个相同种类的任务之间必须有长度为 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。 
# 
#  你需要计算完成所有任务所需要的最短时间。 
# 
#  
# 
#  示例 ： 
# 
#  输入：tasks = ["A","A","A","B","B","B"], n = 2
# 输出：8
# 解释：A -> B -> (待命) -> A -> B -> (待命) -> A -> B.
#      在本示例中，两个相同类型任务之间必须间隔长度为 n = 2 的冷却时间，而执行一个任务只需要一个单位时间，所以中间出现了（待命）状态。 
# 
#  
# 
#  提示： 
# 
#  
#  任务的总个数为 [1, 10000]。 
#  n 的取值范围为 [0, 100]。 
#  
#  Related Topics 贪心算法 队列 数组 
#  👍 336 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        """
        思路：
        1.计算出任务种类和任务出现次数，用字典
        2.首先安排出现次数最多的任务，假设任务A,x
        3.执行这些任务的最少时间是 （x-1）*（n+1）+1
        4.在间隔处安排其他任务，则 （x-1）*（n+1）+ 1 + p，p是和任务A出现次数相同的任务数量
        5.加入计算出的时间小于等于len(tasks)，则返回数组长度，意味着间隔处已经安排满了
        复杂度分析：
        时间复杂度O(NlogN)
        空间复杂度O(N)
        """
        # m = len(tasks)
        # if m <= 1:
        #     return m
        # task_map = dict()
        # for task in tasks:
        #     task_map[task] = task_map.get(task, 0) + 1
        # # 按任务出现的次数从大到小排序，返回的是列表嵌套多个元组
        # task_sort = sorted(task_map.items(), key=lambda x:x[1], reverse=True) #
        # max_task_count = task_sort[0][1]
        # res = (max_task_count - 1) * (n+1)
        # for task in task_sort:
        #     if task[1] == max_task_count:
        #         res += 1
        # return res if res >= m else m

        """
        优化：
        不排序
        """
        count = [0] * 26
        # 计算任务出现的次数
        for ch in tasks:
            count[ord(ch) - ord('A')] += 1
        count_max = max(count)
        total = (count_max - 1) * (n + 1)
        for i in count:
            if i == count_max:
                total += 1
        return max(total, len(tasks))

# leetcode submit region end(Prohibit modification and deletion)
