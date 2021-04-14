#https://leetcode.com/problems/linked-list-cycle-ii/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None : return head
        passed_nodes = []
        pointer = head 
        passed_nodes.append(pointer) 
        while(pointer.next != None):
            if(pointer.next in passed_nodes):
                return pointer.next
            else:
                passed_nodes.append(pointer)
            pointer = pointer.next
        
        return None
        
