#https://leetcode.com/problems/reverse-linked-list/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        listNode = []
        pointer = head

        if head == None: return head
        while(pointer):
            listNode.append(pointer)
            pointer = pointer.next
        newList = ListNode()
        pointer = newList
        for i in listNode[::-1]:
            pointer.next = ListNode(i.val)
            pointer = pointer.next
        return newList.next
