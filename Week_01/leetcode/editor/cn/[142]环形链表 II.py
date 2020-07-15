# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。 
# 
#  为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。 
# 
#  说明：不允许修改给定的链表。 
# 
#  
# 
#  示例 1： 
# 
#  输入：head = [3,2,0,-4], pos = 1
# 输出：tail connects to node index 1
# 解释：链表中有一个环，其尾部连接到第二个节点。
#  
# 
#  
# 
#  示例 2： 
# 
#  输入：head = [1,2], pos = 0
# 输出：tail connects to node index 0
# 解释：链表中有一个环，其尾部连接到第一个节点。
#  
# 
#  
# 
#  示例 3： 
# 
#  输入：head = [1], pos = -1
# 输出：no cycle
# 解释：链表中没有环。
#  
# 
#  
# 
#  
# 
#  进阶： 
# 你是否可以不用额外空间解决此题？ 
#  Related Topics 链表 双指针 
#  👍 537 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """
        1.哈希表：分配一个set集合去保存已经访问过的列表节点
        时间复杂度O(N),空间复杂度O(N)
        """
        # visited = set()
        # node = head
        # while node is not None:
        #     if node in visited:
        #         return node
        #     else:
        #         visited.add(node)
        #         node = node.next
        # return None
        """
        2.双指针法：
        走a+nb步一定在环入口
        第一次相遇时满指针已经走了nb步，
        因此第一次相遇后，快指针从链表起始点走a步,慢指针也走a步
        时间复杂度O(N), 空间复杂度为O(1)
        """
        fast, slow = head, head
        while True:
            if not (fast and fast.next):
                return None
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                break
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast


        
# leetcode submit region end(Prohibit modification and deletion)
