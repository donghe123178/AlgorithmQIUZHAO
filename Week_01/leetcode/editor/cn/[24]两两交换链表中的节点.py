# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。 
# 
#  你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。 
# 
#  
# 
#  示例: 
# 
#  给定 1->2->3->4, 你应该返回 2->1->4->3.
#  
#  Related Topics 链表 
#  👍 547 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """
        1.三指针迭代，一个辅助哨兵节点pre指向实际链表头部,但不可移动，用tmp结点代替移动
        需要注意，链表有两种情况，奇数个和偶数个
        时间复杂度O(N),空间复杂度O(1)
        """
        # pre = ListNode(0)
        # pre.next = head
        # tmp = pre
        # while tmp.next and tmp.next.next:  # 循环交换的条件：偶数个结点
        #     slow = tmp.next
        #     fast = tmp.next.next
        #     # 交换
        #     tmp.next = fast
        #     slow.next = fast.next
        #     fast.next = slow
        #     # tmp 指针移动到下一次交换的结点的前一个位置
        #     tmp = slow
        # return pre.next
        """
        2.递归
        最小重复单元：交换完成的子链表
        终止条件：head或head.next为空指针，当前无节点，或者只有一个结点
        """
        if not head or not head.next:
            return head
        next = head.next
        head.next = self.swapPairs(next.next)
        next.next = head
        return next



# leetcode submit region end(Prohibit modification and deletion)
