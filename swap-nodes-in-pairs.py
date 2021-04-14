#https://leetcode.com/problems/swap-nodes-in-pairs/submissions/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapVals(self, node1, node2):
        aux1 = node1.val
        aux2 = node2.val
        
        node1.val = aux2
        node2.val = aux1
        
    def swapPairs(self, head):
        
        tempNode = head
        
        while(tempNode != None ):
            if(tempNode.next != None ):
                self.swapVals(tempNode, tempNode.next)
                tempNode = tempNode.next.next
            else:
                break
            


        return head
