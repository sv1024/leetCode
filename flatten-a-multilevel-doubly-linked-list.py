#https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/submissions/
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if(head == None): return None
        nodes_list = []
        child_nodes = []
        pointer = head
        l2 = []

        while(pointer):
            if(pointer.child):
                child_nodes.append(pointer)
            nodes_list.append(pointer)
            pointer = pointer.next
            
            if(pointer == None):
                while(child_nodes):
                    for i in range(len(l2)):
                        nodes_list.append(l2[i])
                    l2 = nodes_list[nodes_list.index(child_nodes[0]) +1 :]
                    nodes_list = nodes_list[:nodes_list.index(child_nodes[0]) + 1]

                    pointer = child_nodes.pop(0).child
        for i in range(len(l2)):
            nodes_list.append(l2[i])            
        newList = Node(nodes_list[0].val, None, None, None)
        pointer = newList
        for i in range(len(nodes_list)):
            pointer.next = Node(nodes_list[i].val, pointer, None, None)
            pointer = pointer.next
        newList.next.prev = None 
        return newList.next


        
