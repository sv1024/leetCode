#https://leetcode.com/problems/linked-list-cycle/
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
        if head == None : return None
        passed_nodes = []
        pointer = head 
        passed_nodes.append(pointer) 
        while(pointer.next != None):
            if(pointer.next in passed_nodes):
                return True
            else:
                passed_nodes.append(pointer)
            pointer = pointer.next
        return False
            
