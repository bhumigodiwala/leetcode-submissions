# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Approach 1: Recursively

        res = []
        def inorderTraversal(root):
            if root is None :
                return None
            inorderTraversal(root.left)
            res.append(root.val)
            inorderTraversal(root.right)

        inorderTraversal(root)
        return res[k-1]

        # Approach 2: Iteratively using stack

        #  n = Number of elements visited from the tree 
        # n = 0
        # stack = []
        # # Current pointer
        # cur = root

        # while cur:
        #     # Keep going to left
        #     # visit every node of the left subtree
        #     # add current ot stack
        #     stack.append(cur)
        #     cur = cur.left
        
        # while k!= 0:
        #     # One we pop an element fromthe stack we update n 
        #     # means we visited that node completely
        #     node = stack.pop()
        #     k -= 1
        #     if k == 0:
        #         return node.val
        #     # Now got to right subtree
        #     right = node.right
        #     while right:
        #         stack.append(right)
        #         right= right.left
        # return -1