# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。 
# 
#  k 是一个正整数，它的值小于或等于链表的长度。 
# 
#  如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。 
# 
#  
# 
#  示例： 
# 
#  给你这个链表：1->2->3->4->5 
# 
#  当 k = 2 时，应当返回: 2->1->4->3->5 
# 
#  当 k = 3 时，应当返回: 3->2->1->4->5 
# 
#  
# 
#  说明： 
# 
#  
#  你的算法只能使用常数的额外空间。 
#  你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。 
#  
#  Related Topics 链表 
#  👍 638 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        pre = ListNode(0)
        pre.next = head
        cur = pre

        while head:
            tail = cur
            # 查看剩余部分长度是否大于等于K
            for i in range(k):
                tail = tail.next
                if not tail:
                    return pre.next
            nex = tail.next
            # 子链表翻转
            head, tail = self.reverse(head, tail)
            # 把子链表重新接回原链表
            cur.next = head
            tail.next = nex
            cur = tail
            head = tail.next
        return pre.next

    def reverse(self, head, tail):
        pre = tail.next
        p = head
        while pre != tail:
            nex = p.next
            p.next = pre
            pre = p
            p = nex
        return tail, head

# 备注：没懂
# leetcode submit region end(Prohibit modification and deletion)
