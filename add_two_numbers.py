#https://leetcode.com/problems/add-two-numbers/
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        tempNode = l1
        n1 = ""

        while (tempNode != None):
            n1  += str(tempNode.val)
            tempNode = tempNode.next
        tempNode = l2
        n2 = ""
        n1 = n1[::-1]


        while (tempNode != None):
            n2  += str(tempNode.val)
            tempNode = tempNode.next

        n2 = n2[::-1]

        result = str(int(n1) + int(n2))[::-1]


        for i in range(len(result)):
            if i == 0 :
                head = ListNode(result[0])
                linkedList = head
            else:
                head.next = ListNode(result[i])
                head = head.next
        return linkedList
