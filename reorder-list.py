#https://leetcode.com/problems/reorder-list/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isOdd(self, len_str):
        if(len_str % 2 == 0): return False
        return True
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head == None : return None
        else:
            if head.next == None: return head
                
        first_half = []
        half = []
        second_half = []
        pointer = head
        nodes_list = []
        while(pointer != None):
            nodes_list.append(pointer) 
            pointer = pointer.next
        
        if(self.isOdd(len(nodes_list))):
            first_half = nodes_list[0:int(len(nodes_list)/2)]
            second_half = nodes_list[int(len(nodes_list)/2) + 1:len(nodes_list)]
            half = nodes_list[len(nodes_list)/2]
        else:
            first_half = nodes_list[0:int(len(nodes_list)/2)]
            second_half = nodes_list[int(len(nodes_list)/2):len(nodes_list)]
        second_half = second_half[::-1]
        nodes_list.append(pointer)

        for i in range(len(first_half)):
            if(i%2 == 0):
                
                first_half[i].next = second_half[i]
                if(i>0):
                    second_half[i - 1].next = first_half[i]
                    
            else:
                print(second_half[i].val)
                second_half[i - 1].next = first_half[i]
                print(second_half[i].next.val)
                first_half[i].next = second_half[i]
        if(self.isOdd(len(nodes_list) - 1)):
            second_half[len(second_half) - 1].next = half
            half.next = nodes_list[len(nodes_list) - 1]
        else:
            second_half[len(second_half) - 1].next = nodes_list[len(nodes_list) - 1]

