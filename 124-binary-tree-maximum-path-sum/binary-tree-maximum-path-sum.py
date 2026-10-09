# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Define a global variable for the res initialised with the root value

        res = [root.val]

        # Define a recursive function to calculate max path sum with and without the split
        def dfs(root):
            if not root:
                return 0
            
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            # To handle the case when both left and right nodes are negative
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # Compute the path sum WITH left and right split allowed
            res[0] = max(res[0], root.val + leftMax + rightMax)

            # Compute the path sum WITHOUT left and right split allowed
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]