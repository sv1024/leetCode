#https://leetcode.com/problems/palindrome-linked-list/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        listNode = ""
        pointer = head

        if head == None: return True
        while(pointer):
            listNode += str(pointer.val)
            pointer = pointer.next
            
        return listNode == listNode[::-1]
