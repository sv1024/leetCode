#https://leetcode.com/problems/binary-tree-inorder-traversal/submissions/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.values = []
    def inorder(self, root):
        if root:
            self.inorder(root.left)        
            self.values.append(root.val)
            self.inorder(root.right)
    def inorderTraversal(self, root):
        self.inorder(root)
        return self.values
            
            

        
