#https://leetcode.com/problems/deepest-leaves-sum/submissions/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def deepestLeavesSum(self, root):
        values = []
        printLevels(root, values)
        return deepestLeavesSum(values)
        """
        :type root: TreeNode
        :rtype: int
        """

class TreeNode(object):
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key 
        self.level = 0

def printLevels(root, values, level = 0): 
    if root:
        root.level = level
        if(len(values) <= level):
            values.append(0)
        values[level] += root.val
        level += 1
        printLevels(root.left, values, level)        
        printLevels(root.right, values, level)

def deepestLeavesSum(values):
    return values.pop()
