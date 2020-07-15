# 给定一个链表，判断链表中是否有环。 
# 
#  为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。 
# 
#  
# 
#  示例 1： 
# 
#  输入：head = [3,2,0,-4], pos = 1
# 输出：true
# 解释：链表中有一个环，其尾部连接到第二个节点。
#  
# 
#  
# 
#  示例 2： 
# 
#  输入：head = [1,2], pos = 0
# 输出：true
# 解释：链表中有一个环，其尾部连接到第一个节点。
#  
# 
#  
# 
#  示例 3： 
# 
#  输入：head = [1], pos = -1
# 输出：false
# 解释：链表中没有环。
#  
# 
#  
# 
#  
# 
#  进阶： 
# 
#  你能用 O(1)（即，常量）内存解决此问题吗？ 
#  Related Topics 链表 双指针 
#  👍 673 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        """
        1.暴力法:用一个set数据结构存储每个节点地址，循环遍历，检查一个结点是否被访问
        时间和空间复杂度都是O(N)
        """
        # a = set()
        # while head is not None:
        #     if head in hash:
        #         return True
        #     else:
        #         a.add(head)
        #         head = head.next
        # return False

        """
        2.快慢指针
        定义一个快指针和慢指针,每次快指针走2步，慢指针走1步，判断快指针是否与慢指针重逢
        时间复杂度是O(N),空间复杂度O(1)
        """
        # slow = head
        # fast = head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        #     if slow is fast:
        #         return True
        # return False
        """
        3.递归标记法
        把访问过的值都进行赋值，如果链表完全成环，则必会出现重复值
        时间和空间复杂度都是O(N)
        """
        if head is None:
            return False
        if head.val == "dagdabg":
            return True
        head.val = "dagdabg"
        return self.hasCycle(head.next)


# leetcode submit region end(Prohibit modification and deletion)
