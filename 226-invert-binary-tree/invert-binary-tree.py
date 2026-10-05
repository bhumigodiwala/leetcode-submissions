# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Approach 1
        # if not root:
        #     return None

        # left = root.left
        # right = root.right

        # root.left = self.invertTree(right)
        # root.right = self.invertTree(left)
        # return root

        # Approach 2

        if not root:
            return None
        
        # Swap the children
        temp = root.left
        root.left = root.right
        root.right = temp

        # Call recursively to do DFS
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root