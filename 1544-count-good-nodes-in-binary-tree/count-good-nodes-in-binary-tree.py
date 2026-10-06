# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # Use dfs
        def dfs(node, maxVal):
            # if the node is null we return 0
            if not node:
                return 0

            # result is 1 if it is a goodnode
            res = 1 if node.val >= maxVal else 0
            # Update the maxValue so far
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res

        return dfs(root, root.val)