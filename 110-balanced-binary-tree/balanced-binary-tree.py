# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # O(n) time

        # Define a recursive helper dfs method that returns 
        # 1. bool(T/F) - check if tree is balanced
        # 2. height - height of subtree
        # We follow a bottom up approach

        def dfs(root):

            if not root:
                return [True, 0]

            left,right = dfs(root.left), dfs(root.right)
             

            # For balnced check three conditions
            # 1. if bool value for right is True = right[0]
            # 2. if bool value for left is True = left[0]
            # 3. height difference is atmost 1

            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

            return [balanced, 1 + max(left[1], right[1])]

        # Call the dfs method and return the boolean value stored as
        # first element of the output list
        return dfs(root)[0]