#https://leetcode.com/problems/remove-duplicates-from-sorted-list/submissions/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        vals = []
        pointer = head
        if(head == None): return None
        while(pointer != None):  
            if(pointer.val not in vals):
                vals.append(pointer.val)
            pointer = pointer.next
        newList = ListNode()
        tempNode = newList
        for i in range(len(vals)):
            tempNode.next = ListNode(vals[i] )
            tempNode = tempNode.next
        return newList.next
