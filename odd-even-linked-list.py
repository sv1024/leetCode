#https://leetcode.com/problems/odd-even-linked-list/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        evenNodes = []
        oddNodes = []
        pointer = head
        i = 1
        while(pointer):
            if(i%2 == 0):
                evenNodes.append(pointer)
            else:
                oddNodes.append(pointer)
            i += 1
            pointer = pointer.next
        
        newList = ListNode()
        newPointer = newList
        for i in range(len(oddNodes)):
            newPointer.next = ListNode(oddNodes[i].val)
            newPointer = newPointer.next
        
        for i in range(len(evenNodes)):
            newPointer.next = ListNode(evenNodes[i].val)
            newPointer = newPointer.next
            
        return newList.next
            
        
            
            
            
            
            
        
        
        
        
                
        
            
            
