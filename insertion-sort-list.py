#https://leetcode.com/problems/insertion-sort-list/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tempNode = head 
        vals = []
        if(head == None): return None
        while(tempNode != None):
            vals.append(tempNode.val)
            tempNode = tempNode.next
        vals = sorted(vals)
        print(vals)
        
        newList = ListNode()
        pointer = newList
        for i in range(len(vals)):
            pointer.next = ListNode(vals[i])
            pointer = pointer.next 

        head = newList.next
        return head

