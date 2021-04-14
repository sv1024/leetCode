#https://leetcode.com/problems/add-two-numbers-ii/submissions/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        pointer_l1 = l1
        pointer_l2 = l2
        l1_str = ""
        l2_str = ""
        
        while(pointer_l1):
            l1_str += str(pointer_l1.val)
            pointer_l1 = pointer_l1.next
        
        while(pointer_l2):
            l2_str += str(pointer_l2.val)
            pointer_l2 = pointer_l2.next            
        sum_lists = int(l1_str) + int(l2_str) 
        sum_lists = str(sum_lists)

        new_list = ListNode()
        new_pointer = new_list
        for i in range(len(sum_lists)):
            new_pointer.next = ListNode(int(sum_lists[i]))
            new_pointer = new_pointer.next

        return new_list.next
        
