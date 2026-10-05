# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # O(n) time

        res = [0]

        def dfs(root):
            '''
            return the height running through the root node
            '''
            
            if not root:
                # returning height = -1 if root node is null
                return -1

            # find height of the left subtree and right subtree
            left = dfs(root.left)
            right = dfs(root.right)

            # find diameter of current root 
            res[0] = max(res[0], left + right + 2)

            return 1 + max(left, right)

        dfs(root)
        return res[0]