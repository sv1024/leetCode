#https://leetcode.com/problems/copy-list-with-random-pointer/
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head == None: return None
        newList = Node(0)
        pointer = newList
        tempNode = head
        nodeList = []
        copyList = []
        while(tempNode != None):
            nodeList.append(tempNode)
            pointer.next = Node(tempNode.val)
            pointer = pointer.next
            copyList.append(pointer)
            tempNode = tempNode.next
            if(tempNode == None):
                nodeList.append(tempNode)
                copyList.append(None)

        new_pointer = newList.next
        new_temp_node = head
        while(new_pointer != None):
            if(new_temp_node.random != None):
                index = nodeList.index(new_temp_node.random)
            else:
                index = len(nodeList) - 1
            new_temp_node = new_temp_node.next
            new_pointer.random = copyList[index]
            new_pointer = new_pointer.next
            
        return newList.next
                
            

        

