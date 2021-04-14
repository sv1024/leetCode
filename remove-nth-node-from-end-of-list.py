#https://leetcode.com/problems/remove-nth-node-from-end-of-list/
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pointer1 = head
        pointer2 = pointer1
        for i in range(0,n):
            pointer2 = pointer2.next
        if not pointer2:
            return head.next
        while (pointer2 and pointer2.next != None):
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        pointer1.next = pointer1.next.next
        return head
