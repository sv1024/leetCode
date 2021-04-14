#https://leetcode.com/problems/merge-two-sorted-lists/submissions/
class ListNode(object):
    def __init__(self, val= 0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        newList = ListNode()
        tempNode = newList
        
        while(l1 and l2):
            if(l1.val < l2.val):
                tempNode.next = l1 
                tempNode = tempNode.next
                l1 = l1.next
            else:
                tempNode.next = l2
                tempNode = tempNode.next
                l2 = l2.next
        if l1:
            tempNode.next = l1
        if l2:
            tempNode.next = l2            
            
        return newList.next
