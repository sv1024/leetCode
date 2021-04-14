#https://leetcode.com/problems/reverse-linked-list-ii/submissions/

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if head == None: return None
        cont = 1 
        leftA = []
        rightA = []
        to_sort = []
        pointer = head
        while(pointer != None):
            if(cont < left): 
                leftA.append(pointer.val)
            else:
                if(left <= cont <= right):

                    to_sort.append(pointer.val)
                else:
                    rightA.append(pointer.val)
            pointer = pointer.next 
            cont += 1
        
        newList = ListNode
        newPointer = newList
        for i in leftA:
            newPointer.next = ListNode(i)
            newPointer = newPointer.next
            
                
        for i in range( len(to_sort) -1, -1, -1 ):
            newPointer.next = ListNode(to_sort[i])
            newPointer = newPointer.next
        for i in rightA:
            newPointer.next = ListNode(i)
            newPointer = newPointer.next
        
        return newList.next
        
                
                
