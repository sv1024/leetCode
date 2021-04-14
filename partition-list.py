#https://leetcode.com/problems/partition-list/submissions/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if(head == None): return None
        pointer = head
        cont = 0
        wrong = []
        right = []
        while(pointer != None):
            if(pointer.val < x):
                wrong.append(pointer.val)
            else:
                right.append(pointer.val)
            pointer = pointer.next    
            cont += 1
        for i in range(len(right)):
            wrong.append(right[i])
            
        newPointer = ListNode()
        tempNode = newPointer
        
        for i in range(len(wrong)):
            tempNode.next = ListNode(wrong[i])
            tempNode = tempNode.next
            
                        
        return newPointer.next
        
