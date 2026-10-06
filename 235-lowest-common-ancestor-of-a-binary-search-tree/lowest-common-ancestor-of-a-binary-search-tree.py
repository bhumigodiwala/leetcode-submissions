# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # Since we know that it is a Binary Search Tree (BST),
        # the values on the right and greater than the node value
        # and the values on the left are less than the root node value

        # Check if the value of the current node is greater than both p and q, 
        # then there is no point in searching the right tree
        # so we recursively search on the left part of the tree
        
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)

        # Check if the value of the current node is less than both p and q, 
        # then there is no point in searching the left tree
        # so we recursively search on the right part of the tree
        
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        else:
            return root


        # Approach 2: Neetcode solution

        # O(logn) time and O(1) memory

        # curr = root
        # while curr:
        #     if p.val > curr.val and q.val > curr.val:
        #         curr = curr.right
        #     elif p.val < curr.val and q.val < curr.val:
        #         curr = curr.left
        #     else:
        #         return curr 