#https://leetcode.com/problems/split-linked-list-in-parts/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def items(self, root):
        pointer = root 
        cont = 0
        while(pointer):
            cont += 1 
            pointer = pointer.next
        
        return cont
    def isBigger(self,cont, k):
        if(k>cont): return True
        return False
    def evaluateSizes(self, sizes):
        if(sizes[0] > sizes[1]):
            dif = sizes[0] - sizes[1]
            cont = 1
            sizes[0] = sizes[0] - dif
            for i in range(dif):
                sizes[cont+i] += 1
        return sorted(sizes)[::-1]
                
            
    def setSizes(self, cont, k ):
        sizes = []
        if(self.isBigger(cont, k)):
            for i in range(k):
                if(i<cont):
                    sizes.append(1)
                else:
                    sizes.append(0)
        else:
            n = int(cont / k)
            for i in range(k):
                if(i + 1 == k):
                    sizes.append(cont)
                else:
                    sizes.append(n)
                    cont -= n 
        
        return sorted(sizes)[::-1]
            
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        if(k == 1): return [root]
        pointer = root
        lists = []
        sizes = self.evaluateSizes(self.setSizes(self.items(root), k))
        print(sizes)
        for i in sizes:
            newNode = ListNode()
            tempNode = newNode
            if(i == 0):
                lists.append(None)    
            for j in range(i):
                tempNode.next = ListNode(pointer.val) 
                tempNode = tempNode.next
                pointer = pointer.next
                if(j == 0):
                    lists.append(tempNode)    

        
        
        return lists
        
        
        
