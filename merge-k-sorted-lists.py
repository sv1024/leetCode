#https://leetcode.com/problems/merge-k-sorted-lists/
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        array = []
        newList = ListNode
        tempNode = newList

        for i in lists:
            if i != None:
                while (i != None):
                    array.append(i.val)
                    i = i.next

            else:
                
                continue
        
        
        array = sorted(array)
        
        for i in range(len(array)):
            tempNode.next = ListNode(array[i])
            tempNode = tempNode.next
        

        if(len(array) == 0):
            return None
        
        return newList.next
        

        
        
        
        
    
