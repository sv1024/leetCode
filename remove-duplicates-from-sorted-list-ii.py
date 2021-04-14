#https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/submissions/
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    
    def deleteDuplicates(self, head):
        cont = 0
        array = []
        pointer = head
        if (head == None):
            return None
        while(pointer.next != None):
            if(pointer.val == pointer.next.val):
                array.append(cont)
                array.append(cont + 1)
            cont+=1
            pointer = pointer.next

        cont = 0
        newPointer = head
        newList = ListNode()
        tempNode = newList

        while(newPointer != None):
            if(cont not in array):
                tempNode.next = ListNode(newPointer.val)
                tempNode = tempNode.next                
            cont +=1
            newPointer = newPointer.next
        return newList.next
            
                

            

        
