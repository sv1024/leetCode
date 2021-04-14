#https://leetcode.com/problems/rotate-list/submissions/
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        if(head == None): return None
        else:
            if(k == 0):
                return head
        tempNode = head
        lenght = 1
        while(tempNode != None):
            if(tempNode.next == None):
                tempNode.next = head
                break
            else:
                tempNode = tempNode.next   
                lenght += 1
        newHead = head
        lastNode = tempNode
        k = k%lenght
        if(k == 0):
            lastNode.next = None
            return head
        for i in range(k):
            if(i != 0):
                while(newHead.next != lastNode):
                    newHead = newHead.next    
                lastNode = newHead
        newNode = ListNode()
        newHead = newNode
        pointer = lastNode
        newNode.next = pointer
        while(pointer.next != lastNode):
            newNode.next = ListNode(pointer.val)
            newNode = newNode.next
            pointer = pointer.next
        newNode.next = ListNode(pointer.val)
        return newHead.next
        
