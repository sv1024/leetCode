#https://leetcode.com/problems/intersection-of-two-linked-lists/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None: return None
        pointer_hA = headA
        pointer_hB = headB
        setA = set()

        while(pointer_hA != None):
            setA.add(pointer_hA)
            pointer_hA = pointer_hA.next

        while(pointer_hB != None):
            if pointer_hB in setA: 
                return pointer_hB             
            pointer_hB = pointer_hB.next

        return None
    
