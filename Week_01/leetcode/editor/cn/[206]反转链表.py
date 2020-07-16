# 反转一个单链表。 
# 
#  示例: 
# 
#  输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL 
# 
#  进阶: 
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？ 
#  Related Topics 链表 
#  👍 1091 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """
        1.迭代方法，快慢指针,时间复杂度O(N)
        """
        # pre = None
        # cur = head
        # while cur is not None:
        #     tmp = cur.next # 借助辅助空间
        #     cur.next = pre
        #     pre = cur
        #     cur = tmp
        # return pre
        """
        2.递归
        终止条件：当前节点或者下一个节点==None
        时间复杂度是O(N),空间复杂度是O(N),递归调用会使用隐士栈空间
       """
        # def helper (head):
        #     if head == None or head.next == None:
        #         return head, head
        #     pre, cur = helper(head.next)
        #     cur.next = head
        #     head.next = None  # 断开，防止循环
        #     return pre, head
        # pre, cur = helper(head)
        # return pre
        # 递归的另一种写法
        if head is None or head.next is None: # 注意这里的写法
            return head
        pre = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return pre



# leetcode submit region end(Prohibit modification and deletion)
