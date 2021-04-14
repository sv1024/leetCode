#https://leetcode.com/problems/remove-linked-list-elements/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if (head == None): return None
        if (head.next == None):
            if (head.val == val):
                return None
            else:
                return head
            
        pointer = head 
        tempP = head
        listNodes = []
        while(pointer):
            if(pointer.val == val):
                head = head.next
                pointer = head
            else:
                tempPointer = pointer.next 
                while(tempPointer):
                    if(tempPointer.val != val):
                        pointer.next = tempPointer
                        break 
                    else:
                        if(tempPointer.next):
                            tempPointer = tempPointer.next
                        else:
                            pointer.next = None
                            break
                
                
                pointer = pointer.next 
    
        return head
