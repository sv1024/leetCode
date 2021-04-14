#https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapVals(self, node_1, node_2):
        val1, val2 = node_1.val, node_2.val
        node_1.val = val2
        node_2.val = val1
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        pointer = head 
        nodes_list = []
        while(pointer):
            nodes_list.append(pointer)
            pointer = pointer.next
        self.swapVals( nodes_list[k - 1], nodes_list[len(nodes_list) - k])

        return head
